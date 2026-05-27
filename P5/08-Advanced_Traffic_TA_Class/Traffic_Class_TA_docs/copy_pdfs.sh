#!/bin/bash
# Script: copy_pdfs.sh
# Purpose: Copy each main.pdf from P* folders into V2 with the folder name

# Create destination folder if it doesn't exist
mkdir -p V2

# Loop through all folders starting with P
for d in P*; do
    if [ -f "$d/main.pdf" ]; then
        cp "$d/main.pdf" "V2/${d}.pdf"
        echo "Copied $d/main.pdf → V2/${d}.pdf"
    else
        echo "⚠️  No main.pdf found in $d — skipped."
    fi
done

echo "✅ Done!"

