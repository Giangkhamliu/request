# import requests module
import requests
from requests.auth import HTTPBasicAuth
  
# Making a get request
response = requests.get('https://github.com/Giangkhamliu, ',
            auth = HTTPBasicAuth('Giangkhamliu', '21jan2021'))
  
# print request object
print(response)

