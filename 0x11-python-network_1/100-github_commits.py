#!/usr/bin/python3
""" Python script that takes 2 arguments in order to list 10 commits
(from the most recent to oldest) of the repository “rails” by the user “rails”
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10"\
            .format(sys.argv[2], sys.argv[1])
    r = requests.get(url)
    commits = r.json()
    for commit in commits:
        print("{}: {}".format(commit.get("sha"),
                              commit.get("commit").get("author").get("name")))
