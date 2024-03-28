#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response (decoded in utf-8)"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    r = request.Request(url)
    try:
        with request.urlopen(r) as response:
            print(response.read().decode())
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
