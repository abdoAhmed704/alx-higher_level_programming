#!/usr/bin/python3
"""takes your GitHub credentials uses the GitHub API to display your id"""


if __name__ == '__main__':
    import sys
    import requests
    import json

    headers = {'Accept': 'application/vnd.github+json',
               'Authorization':  f'Bearer {sys.argv[2]}',
               'X-GitHub-Api-Version': '2022-11-28'}
    response = requests.get('https://api.github.com/user', headers=headers,)
    try:
        resp = response.json()
        if (resp):
            print(f'{resp.get("id")}')
    except json.JSONDecodeError:
        print('None')
