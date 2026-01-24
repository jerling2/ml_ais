#!/bin/bash

# I check if I have the zip file before downloading it.
# I download the large zip file into the ARCHIVE directory.
# I unzip the file and place its contents in the DATA directory.

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
DATA_DIR="$SCRIPT_DIR/../hawaii_data"
ARCHIVE="$SCRIPT_DIR/../hawaii_archive"
ZIP_FILE="$ARCHIVE/HawaiiCoast_GT.zip"
TARGET_DATASET="HawaiiCoast_GT/AIS_data/Hawaii_2020_12.csv"

# Verify zenodo-get is installed
if ! command -v zenodo_get &> /dev/null
then
    echo "zenodo-get not found."
    echo "run \`pip install zenodo-get\`"
    exit 1
fi

# Create both directories (DATA_DIR and ARCHIVE)
mkdir -p "$DATA_DIR" "$ARCHIVE"

if [ -f "$ZIP_FILE" ]; then
    echo "Found existing archive at $ZIP_FILE. Skipping download."
else
    echo "Archive not found. Fetching from Zenodo..."
    # We cd into the archive folder so zenodo_get drops the file there
    if ( cd "$ARCHIVE" && zenodo_get 10.5281/zenodo.8253611 ); then
        echo "Download completed successfully."
    else
        echo "Error: zenodo_get failed to download the dataset." >&2
        exit 1
    fi
fi

# 4. Extract into the main data directory
echo "Extracting data to $DATA_DIR..."

# -n ensures we don't overwrite/re-extract if the CSVs are already there
# -j junk paths (prevents creating nested folders inside hawaii_data)
unzip -nqj "$ZIP_FILE" "$TARGET_DATASET" -d "$DATA_DIR"

if [ $? -eq 0 ]; then
    echo "Successfully extracted. Archive preserved in $ARCHIVE."
else
    echo "Extraction failed. Please check if unzip is installed."
fi

echo "Process complete."