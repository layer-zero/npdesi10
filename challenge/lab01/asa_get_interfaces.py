#!/usr/bin/env python  # recommended shebang to use in Python scripts

# perform imports as required
import requests
import json

# The HTTPBasicAuth simplifies performing authentication for you
from requests.auth import HTTPBasicAuth
# Disable Python warnings when using self-signed / insecure certs
requests.packages.urllib3.disable_warnings()

# main entry point to the script
if __name__ == "__main__":

    auth = HTTPBasicAuth('cisco', 'cisco')

    url = 'https://asa/api/monitoring/device/interfaces'
    # simply use the get method and pass the URL, then verify and auth params 
    # again, we are not verifying the SSL certificate
    response = requests.get(url, verify=False, auth=auth)
    # As seen previously in the NX-API OnBox Python, we sometimes need to
    # work with JSON string objects and need to use json.loads to load it as
    # a JSON object, i.e. dictionary in Python. 

    # Two response attributes are shown below.  status_code and text: they
    # are respectively the HTTP sttaus code of the response and the actual 
    # response itself.
    print 'Status Code: ' + str(response.status_code)
    if response.text:
        parse = json.loads(response.text)
        print json.dumps(parse, indent=4)
