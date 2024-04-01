#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    headers = {'Authorization': f'Bearer {sys.argv[2]}',
               'X-GitHub-Api-Version': '2022-11-28',
               'Accept': 'application/vnd.github.v3+json'}
    url = 'https://api.github.com/user'
    req = requests.get(url, headers=headers)
    print(req.json().get('id'))
