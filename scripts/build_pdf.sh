#!/usr/bin/env bash
set -euo pipefail
if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc not found. Install with: brew install pandoc" >&2
  exit 1
fi
mkdir -p preprint
pandoc \
  --from markdown+smart+implicit_figures+link_attributes \
  --to pdf \
  --metadata title="ConsciOS v1.0: A Viable Systems Architecture for Human and AI Alignment" \
  --pdf-engine=tectonic \
  --resource-path=. \
  --output preprint/ConsciOS_v1.0_preprint.pdf \
  paper-edited.md
echo "Wrote preprint/ConsciOS_v1.0_preprint.pdf"
