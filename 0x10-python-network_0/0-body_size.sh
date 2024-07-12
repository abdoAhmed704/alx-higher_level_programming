#!/bin/bash

# Check if the script is given exactly one argument
curl -s -o /dev/null -w '%{size_download}' "$url"
