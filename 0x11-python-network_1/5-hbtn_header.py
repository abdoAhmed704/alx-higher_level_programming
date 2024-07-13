#!/usr/bin/python3
"""Fetching URL"""


if __name__ == "__main__":
    import requests
    import sys
    res = requests.get(sys.argv[1])
    print(res.headers.get("X-Request-Id"))
