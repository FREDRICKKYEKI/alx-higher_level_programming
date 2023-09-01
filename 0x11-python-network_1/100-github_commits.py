#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge.
    -The first argument will be the repository name
    -The second argument will be the owner name
    -You must use the packages requests and sys
    -You are not allowed to import packages other than requests and sys
    -You don’t need to check arguments passed to the script (number or type)
    -Only 17% of applicants for a backend position at Holberton finished this task
    in less than 15 minutes.
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    try:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
        req = get(url)
        json = req.json()
        for i in range(0, 10):
            print("{}: {}".format(json[i].get('sha'), json[i].get('commit')
                                  .get('author').get('name')))
    except:
        pass
