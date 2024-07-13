#!/usr/bin/python3
"""takes in a URL and an email,
sends a POST request to the passed URL with
the email as a parameter, and displays
the body of the response"""


if __name__ == "__main__":
    import sys
    import urllib.parse
    import urllib.request

    URL = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("utf-8")
    req = urllib.request.Request(URL, data=data)

    with urllib.request.urlopen(req) as res:
        body = res.read().decode('utf-8')
        print(body)
