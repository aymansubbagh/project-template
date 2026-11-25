#!/usr/bin/env bash
# Download every raw input this project uses, by accession or URL, and verify checksums.
# Record each source, version, licence and access date in docs/DATA.md.
set -euo pipefail

RAW_DIR="$(dirname "$0")/../data/raw"
mkdir -p "$RAW_DIR"

# Example (replace with the project's real sources):
# curl -L -o "$RAW_DIR/genome.fna.gz" "https://..."
# echo "<sha256>  $RAW_DIR/genome.fna.gz" | shasum -a 256 -c -

echo "No data sources defined yet. Edit scripts/get_data.sh."
