#!/usr/bin/python3
"""list 10 commits of the repository “rails”"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url)
    commits = req.json()
    try:
        for x in range(10):
            print("{}: {}".format(
                commits[x].get("sha"),
                commits[x].get("commit").get("author").get("name")))
    except IndexError:
        pass
