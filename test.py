import requests

print('Hello there!')

response = requests.get('https://example.com')
print(response.text)
