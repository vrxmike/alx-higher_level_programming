#!/usr/bin/python3
"""Searching json"""
import sys
import requests


if __name__ == "__main__":
    value = {'q': ""}
    if len(sys.argv) > 1:
        value["q"] = sys.argv[1]
    response = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        empty = ["", {}, None]
        if "id" not in response.json().keys() or "name" \
                not in response.json().keys():
            print("No result")
        else:
            print("[{}] {}".format(response.json().get("id"),
                                   response.json().get("name")))
    except ValueError:
        print("Not a valid JSON")
