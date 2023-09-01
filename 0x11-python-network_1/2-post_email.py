#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8)
    - The email must be sent in the email variable
    - You must use the packages urllib and sys
    - You are not allowed to import packages other than urllib and sys
    - You don't need to check arguments passed to the script (number or type)
    - You must use the with statement
"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    request_ = request.Request(sys.argv[1], data)
    with request.urlopen(request_) as response:
        body = response.read()
        print(body.decode('utf-8'))
