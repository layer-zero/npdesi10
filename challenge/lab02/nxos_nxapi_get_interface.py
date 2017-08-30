#!/usr/bin/env python

"""NPDESI challenge lab 2 task 1: Consume NX-API with Python"""

import requests
import json

device_user = 'cisco'
device_pwd = 'cisco'
device_name = 'nxosv'

def get_mgmt_intf(device_name, username, password):
    url = 'http://' + device_name + '/ins'
    auth = requests.auth.HTTPBasicAuth(username, password)
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show interface mgmt0",
            "output_format": "json"
        }
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
    response_body = json.loads(response.text)['ins_api']['outputs']['output']['body']
    interface = response_body['TABLE_interface']['ROW_interface']
    return interface

def main():
    mgmt_interface = get_mgmt_intf(device_name, device_user, device_pwd)
    print 'Management Interface Information:'
    print 'IP Address:     {}/{}'.format(mgmt_interface['eth_ip_addr'],mgmt_interface['eth_ip_mask'])
    print 'Speed:          {}'.format(mgmt_interface['eth_speed'])
    print 'State:          {}'.format(mgmt_interface['state'])
    print 'MTU:            {}'.format(mgmt_interface['eth_mtu'])


if __name__ == "__main__":
    main()