'''Reads a list of IP/domain from a source, checks their reputation in VirusTotal, and returns result
'''

import json
import requests
from pprint import pprint

def is_ip(address):
    return address.replace('.', '').isnumeric()

new_list = []

query =  "<Insert list of IP/Domain here>"
for item in query:
    if(is_ip(item) == True):
        api_u = "https://www.virustotal.com/api/v3/ip_addresses/"
        api_url = api_u + item
    else:
        item = item.strip("https://") #strips leading and trailing characters including / to retain pure URL
        api_ip = "https://www.virustotal.com/api/v3/domains/"
        api_url = api_ip + item
    header = {
            "Accept":"application/json",
            "x-apikey":"<Your API Key here>"
    }
    response = requests.request(method='GET',url=api_url,headers=header).json()
    stats = response['data']['attributes']['last_analysis_stats']
    new_list.append(stats)
    stats['IoC'] = item
    

print(new_list)
