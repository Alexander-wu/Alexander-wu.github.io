"""Refresh the public Scholar count; never replace good data with a failed fetch."""
import json
import os
import re
import time
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


class CitationTable(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.in_count = False
        self.counts = []
        self.value = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "table" and attrs.get("id") == "gsc_rsb_st":
            self.in_table = True
        if self.in_table and tag == "td" and "gsc_rsb_std" in attrs.get("class", "").split():
            self.in_count = True
            self.value = ""

    def handle_data(self, data):
        if self.in_count:
            self.value += data

    def handle_endtag(self, tag):
        if tag == "td" and self.in_count:
            self.counts.append(self.value.strip())
            self.in_count = False
        if tag == "table":
            self.in_table = False


def parse_citations(html):
    table = CitationTable()
    table.feed(html)
    # All-time and recent citations, h-index, i10-index: do not use article counts.
    if len(table.counts) != 6 or not re.fullmatch(r"[0-9]+(?:,[0-9]{3})*", table.counts[0]):
        raise ValueError("Scholar statistics unavailable (blocked response or changed markup)")
    return int(table.counts[0].replace(",", ""))


def fetch_citations(scholar_id):
    url = "https://scholar.google.com/citations?" + urlencode({"user": scholar_id, "hl": "en"})
    request = Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US,en;q=0.9"})
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30) as response:
                html = response.read().decode(response.headers.get_content_charset() or "utf-8", errors="replace")
            return parse_citations(html)
        except Exception:
            if attempt == 2:
                raise
            time.sleep(5 * (attempt + 1))


def save_citations(root, scholar_id, citations):
    if type(citations) is not int or citations < 0:
        raise ValueError("Invalid citation count")
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    data = {"scholar_id": scholar_id, "citations": citations, "updated_at": now}
    index = root / "index.html"
    html, replacements = re.subn(
        r'(<strong id="scholar-citation-count"[^>]*>)[^<]*(</strong>)',
        lambda m: m[1] + format(citations, ",") + m[2], index.read_text(encoding="utf-8"),
    )
    if replacements != 1:
        raise ValueError("Expected exactly one citation counter in index.html")
    # Build both outputs before writing, including the no-JavaScript fallback.
    output = root / "citation-data.json"
    temp = output.with_suffix(".json.tmp")
    temp.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    temp.replace(output)
    index.write_text(html, encoding="utf-8")


def main():
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "HdXMhfcAAAAJ")
    citations = fetch_citations(scholar_id)
    save_citations(ROOT, scholar_id, citations)
    print(f"Google Scholar citations: {citations}")


if __name__ == "__main__":
    main()
