#!/bin/bash
# This script returns the size of the response body type
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2
