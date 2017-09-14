#!/usr/bin/env python

"""NPDESI challenge lab 1 task 4: Construct Python Script Consuming ASA API"""

import requests
import json
requests.packages.urllib3.disable_warnings()

def main():
    auth = requests.auth.HTTPBasicAuth('cisco', 'cisco')
    url = 'https://asa/api/objects/networkservices/ssh-alt'
    response = requests.delete(url, verify=False, auth=auth)
    print 'Status Code: ' + str(response.status_code)
    if response.text:
        parse = json.loads(response.text)
        print json.dumps(parse, indent=4)


if __name__ == "__main__":
    main()

