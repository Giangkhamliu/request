# # Let’s try making a request to github’s APIs for example purposes.

# import requests
# # Making a GET request
# r = requests.get('https://github.com/Giangkhamliu')
# # check status code for response received
# # success code - 200
# print(r)
# # print content of request
# print(r.content)


import requests
# to add URL parameters to our GET requests, we  will create a dictionary 
# above the response object called payload with two parameters names
payload={"firstname":"Grace","Lastname":"Pamei"}
r=requests.get("https://httpbin.org/get",params=payload)
print(r.headers)#response.headers returns a dictionary of response headers.
# print(r.content)# to view the content from the url
# print(r.text)#to view content 
# print(r.url)# r.url will reveal the full URL and after ? indicating the start of query string.
# print(r.status_code)# to view the response code we use status_code, for successful it is 200