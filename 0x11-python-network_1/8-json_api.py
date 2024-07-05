#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter."""

import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"

    data = {'q': letter}

    response = requests.post(url, data=data)

    try:
        parsed_response = response.json()

        if parsed_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(parsed_response.get(
                "id"), parsed_response.get("name")))
    except ValueError:
        print("Not a valid JSON")
