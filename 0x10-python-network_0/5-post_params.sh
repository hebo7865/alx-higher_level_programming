#!/bin/bash
#sends a POST request to the passed URL, and displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be there for PLD" "$1"