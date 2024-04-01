#!/usr/bin/python3
"""
 sends a request to the URL and displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if (req.ok):
        print(req.text)
    else:
        print(f"Error code: {req.status_code}")
