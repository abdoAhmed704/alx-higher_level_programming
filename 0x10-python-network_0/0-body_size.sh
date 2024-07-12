#!/bin/bash

# Check if the script is given exactly one argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL passed as argument
url=$1

# Use curl to fetch the URL and get the size of the response body in bytes
# Use the -s option to silence curl's progress output
# Use the -o option to write output to a file, here /dev/null to discard the body
# Use the -w option to format the output, here '%{size_download}' to get the size in bytes
size=$(curl -s -o /dev/null -w '%{size_download}' "$url")

# Print the size of the response body
echo "$size"

