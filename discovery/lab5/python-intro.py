#!/usr/bin/env python

"""NPDESI lab 5 task 2: Writing a Network Script"""

if __name__ == '__main__':
	facts_1 = {'os': '7.2', 'fqdn': 'cisco.com', 'location': 'sjc', 'vlans_list': [1,5,10], 'neighbors': ['sw2', 'sw3']}
	facts_2 = {'os': '7.3', 'fqdn': 'cisco.com', 'location': 'syd', 'vlans_list': [1,10,20], 'neighbors': ['s1', 's3']}
	facts_3 = {'os': '7.2', 'fqdn': 'cisco.com', 'location': 'nyc', 'vlans_list': [1,4,20], 'neighbors': ['s1', 's2']}

	facts = {'sw1': facts_1, 'sw2': facts_2, 'sw3': facts_3}
	print 'sw1 facts:'
	print facts['sw1']

	vlans = facts['sw2']['vlans_list']
	print 'sw2 vlans:'
	for vlan in vlans:
		print vlan

	print "sw2's second neighbor:"
	print facts['sw2']['neighbors'][1]

	print "sw3's second neighbor:"
	print facts['sw2']['neighbors'][0]
