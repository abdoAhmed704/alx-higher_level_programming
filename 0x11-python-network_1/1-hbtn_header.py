#!/usr/bin/python3
"""get X-Request-Id"""


if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as res:
        print(dict(res.getheaders()).get('X-Request-Id'))
