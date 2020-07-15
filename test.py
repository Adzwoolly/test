import requests

print('Hello there!')

response = requests.get('example.com')
print(response.text)
