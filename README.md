# Hao Wu Homepage

This is a static academic homepage that can be deployed directly on GitHub Pages, Netlify, or Vercel.

## Deploy on GitHub Pages

1. Create a GitHub repository.
2. Upload all files in this directory to the repository root.
3. Go to `Settings` -> `Pages`.
4. Set source to `Deploy from a branch`.
5. Choose branch `main` and folder `/root`.
6. Save and wait for the site to publish.

## Notes

- Keep `index.html` in the repository root.
- Keep folders such as `Image/`, `papers/`, `log/`, and `assets/` unchanged so relative paths continue to work.
- Replace the GitHub button link in `index.html` once the final GitHub profile URL is confirmed.

## Google Scholar citations

The homepage reads `citation-data.json`. `scripts/update_citations.py` fetches
this profile's all-time count using the Python standard library, with bounded
retries and timeouts. A successful fetch updates both JSON and the HTML fallback.
The badge tooltip shows the last successful fetch time; after 48 hours it flags
the data as delayed. Blocked responses preserve the previous data and timestamp.

Pages uses **GitHub Actions** as its publishing source. Every push explicitly
deploys the site. The manual **Run workflow** action also attempts a Scholar
refresh before deploying, and reports a failure if Google blocks the request.

On 2026-09-25, fetching succeeded on the owner's Mac (1,550 citations) but
Google returned HTTP 403 to GitHub-hosted runners. Cloud scheduling is therefore
not enabled. The optional `scripts/sync_citations_local.sh` supports a dedicated
local clone via `CITATION_SYNC_DIR`, using existing `gh` authentication. Installing
a local six-hour timer requires the owner's confirmation; the Mac must be awake
and online. The helper refuses to overwrite tracked local changes.

Run checks with:

```sh
python -m unittest discover -s scripts -p 'test_*.py'
```
