#!/bin/bash
# Sends a POST request with data passed as parameters
curl -sLd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
