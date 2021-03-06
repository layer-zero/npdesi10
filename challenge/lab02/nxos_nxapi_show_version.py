#!/usr/bin/env python

"""NPDESI challenge lab 2 task 1: Consume NX-API with Python"""

import requests
import json
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    auth = HTTPBasicAuth('cisco', 'cisco')
    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show version",
            "output_format": "json"
        }
    }
    url = 'http://nxosv/ins'

    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)

    print 'Status Code: ' + str(response.status_code)
    rx_object = json.loads(response.text)
    print json.dumps(rx_object, indent=4)
    print 'OS: ', rx_object['ins_api']['outputs']['output']['body']['sys_ver_str']

