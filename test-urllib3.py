import config
import urllib3
http = urllib3.PoolManager()
response = http.request('GET', config.url)
print(response.data)