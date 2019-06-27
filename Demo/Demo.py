import requests

# get 请求
# ret = requests.get('https://github.com/timeline.json')

#带参数的get请求
payload = {'key1': 'value1', 'key2': 'value2'}
ret = requests.get("http://httpbin.org/get", params=payload)

print ret.url
print ret.text
