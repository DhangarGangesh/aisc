#!/usr/bin/env bash
set -u
for file in [0-9][0-9]_*.py; do
    echo "========== $file =========="
    python3 "$file" || echo "ERROR: $file"
done
