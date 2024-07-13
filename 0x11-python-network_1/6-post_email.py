#!/usr/bin/python3
"""posting email in URL"""


if __name__ == "__main__":
    import requests
    import sys
    pram = {"email": sys.argv[2]}
    res = requests.post(sys.argv[1], data=pram)
    print('Your email is:', res.json()['form'])
