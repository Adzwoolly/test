import requests

print('Hello there!')

response = requests.get('https://example.com')
print(response.text)

with open('example.html', 'w') as file:
    file.write(response.text)
