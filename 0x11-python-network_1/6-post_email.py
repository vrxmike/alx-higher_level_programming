#!/usr/bin/python3
"""Script that takes in a url and email and sends a POST request"""
import requests
import sys


if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]
    response = requests.post(url, data={'email': email})
    print(response.text)
