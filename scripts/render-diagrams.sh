#!/bin/sh
set -eu

: "${PUPPETEER_EXECUTABLE_PATH:?Set PUPPETEER_EXECUTABLE_PATH to a local Chromium or Chrome executable}"

for source in diagrams/*.mmd; do
  output="${source%.mmd}.svg"
  ./node_modules/.bin/mmdc -i "$source" -o "$output" -b white -t neutral --no-font-embed -c diagrams/mermaid-config.json
done
