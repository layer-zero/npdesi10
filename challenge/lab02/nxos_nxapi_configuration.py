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

    commands = ['vlan 150', 'exit', 'interface Eth2/5', 'switchport', 'switchport access vlan 150']
    command_string = ''
    for command in commands:
        if command_string == '':
            command_string = command
        else:
            command_string = command_string + ' ;' + command
    print command_string

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_conf",
            "chunk": "0",
            "sid": "1",
            "input": command_string,
            "output_format": "json"
        }
    }
    url = 'http://nxosv/ins'

    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
    rx_object = json.loads(response.text)

    print json.dumps(rx_object, indent=4)

