import requests
payload = {'url': 'ebay.com'}
r = requests.get('http://69.181.224.185:8080', params=payload)

print r.text
