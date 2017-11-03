#!/usr/bin/env python
"""
This script performs the same operations as NPDESI challenge lab 6 task 1: Consume NETCONF with Python
It uses the ydk-py library instead of embedding the XML directly inside the script.
For documentation about the object structures and ydk-py in general visit:
http://ydk.cisco.com/py/docs/gen_doc_df76b47e76a58aa15aee29b3b0484ba370fd9172.html 
"""

from ydk.types import Empty
from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_ifmgr_cfg

provider = NetconfServiceProvider(address='172.16.1.14', port=830, username="cisco", password="cisco", protocol="ssh")
crud = CRUDService()

ifcfg = Cisco_IOS_XR_ifmgr_cfg.InterfaceConfigurations()
# This instantiates a list of interface configuration objects.

interface_config = ifcfg.InterfaceConfiguration()
# This instantiates an interface configuration object
interface_config.active = 'act'
interface_config.interface_name = 'Loopback100'
interface_config.interface_virtual = Empty()
# This object needs to be present to trigger creation of the virtual interface, but in itself it has no value.

primary_ip = interface_config.ipv4_network.addresses.Primary()
# This instantiates a primary IP address object. This is done because Primary is a presence class.
# As a result it will be assigned the 'None' value when instantiated normally. Therefore we must specifically
# create a primary IP address instance and then attach it to the configuration.
primary_ip.address = '100.100.1.1'
primary_ip.netmask = '255.255.255.0'
interface_config.ipv4_network.addresses.primary = primary_ip
# This attaches the primary ip address object to the interface configuration object.

ifcfg.interface_configuration.append(interface_config)
# This adds the interface configuration to the list of configuration objects.

interface_config = ifcfg.InterfaceConfiguration()
interface_config.active = 'act'
interface_config.interface_name = 'GigabitEthernet0/0/0/0'
primary_ip = interface_config.ipv4_network.addresses.Primary()
primary_ip.address = '10.23.23.1'
primary_ip.netmask = '255.255.255.0'
interface_config.ipv4_network.addresses.primary = primary_ip
secondary_ips = interface_config.ipv4_network.addresses.Secondaries()
secondary_ip = secondary_ips.Secondary()
secondary_ip.address = '10.32.32.1'
secondary_ip.netmask = '255.255.255.0'
secondary_ips.secondary.append(secondary_ip)
interface_config.ipv4_network.addresses.secondaries = secondary_ips

ifcfg.interface_configuration.append(interface_config)
# This adds configuration for the second interface in a similar manner.

crud.create(provider, ifcfg)
# This pushes the interface configurations to the device.
