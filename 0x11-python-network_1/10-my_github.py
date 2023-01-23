#!/usr/bin/python3
"""Takes my Github creds (username & password)
and uses the Github API to display my ID
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "--main__":
    username = sys.argv[1]
    password = sys.argv[2]

    token = HTTPBasicAuth(username, password)
    request = requests.get('https://api.github.com/user', auth=token)
    print(resquest.json().get("id"))
