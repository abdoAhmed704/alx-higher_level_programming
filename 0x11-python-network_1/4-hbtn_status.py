#!/usr/bin/python3
"""Fetching URL"""


if __name__ == "__main__":
    import requests
    res = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(res.text)}")
    print(f"\t- content: {res.text}")
