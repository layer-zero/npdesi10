#!/usr/bin/env python

"""NPDESI discovery lab 5 task 3: Analyzing and Troubleshooting a Script"""

def print_facts(facts):
    """Print two facts from facts dictionary
    """

    platform = facts.get('platform', 'unknown platform')
    print 'platform', platform

    print 'os', facts['os']


if __name__ == "__main__":

    # Define basic facts about a device
    facts = {'os': '7.2', 'fqdn': 'cisco.com', 'location': 'sjc', 'vlans_list': [1, 5, 10], 'neighbors': ['s2', 's3']}

    # Call print_facts function
    print_facts(facts)

    # Extract neighbors from facts dict and assign to new variable
    neighbors = facts['neighbors']

    # Print each neighbor
    for item in neighbors:
        print item
