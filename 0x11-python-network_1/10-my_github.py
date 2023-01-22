#!/usr/bin/python3
"""Uses github api"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "--main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    response = requests.get("https://api.github.com/user",
                            auth=(username, passwd))
    print(response.json().get("id"))
