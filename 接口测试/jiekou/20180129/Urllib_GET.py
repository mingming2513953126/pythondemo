import urllib.request

url='http://www.baidu.com'

response=urllib.request.Request(url=url)

html=urllib.request.urlopen(response)

print(html.getcode())

print(html.headers)