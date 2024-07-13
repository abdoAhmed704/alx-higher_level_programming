#!/usr/bin/python3
"""hbtn_status"""

if __name__ == "__main__":
    import urllib.request
    with request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        data = res.read()
        print('Body response:$')
        print(f'\t- type: {type(data)}$')
        print(f'\t- content: {data}$')
        print(f'\t- utf8 content: {data.decode("utf-8")}$')
