import requests
payload = {'userName': '13011111103', 'password': '111111'}
r = requests.post("https://t.pangpangpig.com/loginAndBindWeixin.action", data=payload)
print(r.text)