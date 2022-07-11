import requests
payload={"firstname":"Grace","Lastname":"Pamei"}
r=requests.post("https://httpbin.org/post",data=payload)
# print(r.content)
# print(r.text)
# print(r.url)
# print(r.status_code)
print(r.json())#json and content has the same output