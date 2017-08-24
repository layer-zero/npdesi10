#!/usr/bin/env python

"""NPDESI lab 6 task 2: Creating a Python Module"""

PLATFORMS = ['nexus', 'catalyst', 'asr', 'asa']


def vlan_exists(vlan_id):
    vlans_list = [1, 5, 10, 20]
    return vlan_id in vlans_list
