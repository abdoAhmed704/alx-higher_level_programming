#!/usr/bin/python3
"""posting email in URL"""


if __name__ == "__main__":
    import requests
    import sys
    res = requests.get(sys.argv[1])
    if res.status_code > 200:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
