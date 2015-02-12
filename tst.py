import requests
payload = {'url': 'http://ebay.com'}
r = requests.get('http://69.181.224.185:8081', params=payload)

print r.text
