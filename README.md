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

The homepage reads `citation-data.json`; JavaScript cannot fetch Scholar directly
because the site is static and Scholar does not provide browser CORS access.
The **Update citations and deploy homepage** Actions workflow runs every six hours
(at minute 17 UTC) and can also be started with **Run workflow**. GitHub may delay
scheduled jobs, and Google Scholar itself may lag; this is periodic sync, not a
live Google Scholar API.

- `python scripts/update_citations.py` fetches this profile's **all-time** citation
  count using the Python standard library, with bounded retries and timeouts.
- A successful fetch updates both JSON and the HTML fallback, with `updated_at`
  recording the successful fetch time. Hover over the badge to see that time.
- A blocked response or parse failure preserves the previous count and timestamp.
  The workflow still deploys the site, then reports the refresh failure in Actions.
- Pages uses **GitHub Actions** as the publishing source. The same workflow
  explicitly deploys after refreshing data: commits made with `GITHUB_TOKEN`
  do not trigger a second Pages build by themselves. Ordinary pushes also deploy.
- If the timestamp is over 48 hours old, the tooltip indicates a delayed sync.
  Check the failed workflow's fetch step; no CAPTCHA/proxy bypass is attempted.

Run parser and failure-path checks with:

```sh
python -m unittest discover -s scripts -p 'test_*.py'
```
