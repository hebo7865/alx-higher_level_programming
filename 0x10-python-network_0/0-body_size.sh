#!/bin/bash
#get the size of the body of the response to given URL
curl -s "$1" | wc -c
