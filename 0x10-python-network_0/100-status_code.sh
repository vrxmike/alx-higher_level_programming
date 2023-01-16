#!/bin/bash
# Sends a request to a URL and dispaly only the status code
curl -so /dev/null --write-out "%{http_code}" "$1"
