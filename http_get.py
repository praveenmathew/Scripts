import requests

URL = "http://ptl-e34d116d-c53b863a.libcurl.so/pentesterlab"
#cookies = dict(key='please')
#r = requests.get(url = URL, cookies = cookies)
headers = {'Accept-Language' : 'key-please'}
r = requests.get(url = URL, headers = headers)
print (r.content)
