#!/usr/bin/env python

"""NPDESI discovery lab 34 task 1: Validate Device Configurations"""

import unittest
import requests
import json
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

class TestDeviceConfiguration(unittest.TestCase):

    def test_npdesi_snmp_ro(self):
        """Validate npdesi is a configured RO string
        """

        auth = HTTPBasicAuth('cisco', 'cisco')
        headers = { 'Accept': 'application/vnd.yang.data+json'}
        url = 'http://csr1kv/restconf/api/config/native/snmp-server?deep'
        response = requests.get(url, verify=False, headers=headers, auth=auth)

        parse = json.loads(response.text)
        community_list = parse['Cisco-IOS-XE-native:snmp-server']['Cisco-IOS-XE-snmp:community']
        expected = {'name': 'npdesi', 'RO': [None]}
        is_there = expected in community_list
        self.assertTrue(is_there)


    def test_cisco_snmp_ro(self):
        """Validate cisco is a configured RO string
        """

        auth = HTTPBasicAuth('cisco', 'cisco')
        headers = { 'Accept': 'application/vnd.yang.data+json'}
        url = 'http://csr1kv/restconf/api/config/native/snmp-server?deep'
        response = requests.get(url, verify=False, headers=headers, auth=auth)

        parse = json.loads(response.text)
        community_list = parse['Cisco-IOS-XE-native:snmp-server']['Cisco-IOS-XE-snmp:community']
        expected = {'name': 'cisco', 'RO': [None]}
        is_there = expected in community_list
        self.assertTrue(is_there)

    def test_cisco_secure_snmp_rw(self):
        """Validate cisco_secure is a configured RW string
        """

        auth = HTTPBasicAuth('cisco', 'cisco')
        headers = { 'Accept': 'application/vnd.yang.data+json'}
        url = 'http://csr1kv/restconf/api/config/native/snmp-server?deep'
        response = requests.get(url, verify=False, headers=headers, auth=auth)

        parse = json.loads(response.text)
        community_list = parse['Cisco-IOS-XE-native:snmp-server']['Cisco-IOS-XE-snmp:community']
        expected = {'name': 'cisco_secure', 'RW': [None]}
        is_there = expected in community_list
        self.assertTrue(is_there)

    def test_devops_user(self):
        """ Validate existence of devops user
        """
        auth = HTTPBasicAuth('cisco', 'cisco')
        headers = { 'Accept': 'application/vnd.yang.collection+json'}
        url = 'http://csr1kv/restconf/api/config/native/username'
        response = requests.get(url, verify=False, headers=headers, auth=auth)

        parse = json.loads(response.text)
        user_list = parse['collection']['Cisco-IOS-XE-native:username']
        # Strip the passwords from the users if they exist and just extract the usernames.
        username_list = []
        for user in user_list:
            username_list.append(user['name'])
        expected = 'super_user'
        is_there = expected in username_list
        self.assertTrue(is_there)

    def test_super_user(self):
        """ Validate existence of super_user user
        """
        auth = HTTPBasicAuth('cisco', 'cisco')
        headers = { 'Accept': 'application/vnd.yang.collection+json'}
        url = 'http://csr1kv/restconf/api/config/native/username'
        response = requests.get(url, verify=False, headers=headers, auth=auth)

        parse = json.loads(response.text)
        user_list = parse['collection']['Cisco-IOS-XE-native:username']
        # Strip the passwords from the users if they exist and just extract the usernames.
        username_list = []
        for user in user_list:
            username_list.append(user['name'])
        expected = 'super_user'
        is_there = expected in username_list
        self.assertTrue(is_there)



if __name__ == "__main__":
    unittest.main()

              
