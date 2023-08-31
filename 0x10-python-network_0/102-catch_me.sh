#!/bin/bash

# Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes
# the server to respond with a message containing You got me!, in the body of the
# response.
#    - You have to use curl
#    - You are not allow to use echo, cat, etc. to display the final result

curl -s -X PUT -d "user_id=98" "0.0.0.0:5000/catch_me"
