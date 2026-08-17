import json
import os
from datetime import datetime, timezone
from pathlib import Path

from scholarly import scholarly


scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "HdXMhfcAAAAJ")
author = scholarly.search_author_id(scholar_id)
scholarly.fill(author, sections=["basics", "indices"])

citations = author.get("citedby")
if not isinstance(citations, int):
    raise RuntimeError("Google Scholar did not return a valid citation count")

data = {
    "scholar_id": scholar_id,
    "citations": citations,
    "updated_at": datetime.now(timezone.utc).isoformat(),
}

output_path = Path(__file__).resolve().parents[1] / "citation-data.json"
output_path.write_text(
    json.dumps(data, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)

print(f"Updated Google Scholar citations: {citations}")
