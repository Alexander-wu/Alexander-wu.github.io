#!/bin/bash
# Run from a dedicated clone, never the editable homepage working copy.
set -euo pipefail
export PATH="$HOME/.local/bin:/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
: "${CITATION_SYNC_DIR:?Set CITATION_SYNC_DIR to the dedicated homepage clone}"
cd "$CITATION_SYNC_DIR"
if [[ -n "$(git status --porcelain --untracked-files=no)" ]]; then
  echo 'Refusing to overwrite local tracked changes in the citation-sync clone.' >&2
  exit 1
fi
git -c credential.helper= -c 'credential.helper=!gh auth git-credential' pull --ff-only origin main
python3 scripts/update_citations.py
git add citation-data.json index.html
if ! git diff --cached --quiet; then
  git -c user.name='Hao Wu' -c user.email='133833074+Alexander-wu@users.noreply.github.com' commit -m 'Refresh Google Scholar citations'
  git -c credential.helper= -c 'credential.helper=!gh auth git-credential' push origin HEAD:main
fi
