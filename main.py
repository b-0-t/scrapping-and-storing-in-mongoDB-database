# install all dependecies 

import requests
from bs4 import BeautifulSoup as bs

# inspecting indeed.com to get a overview 


job="python+developer"

url = "https://in.indeed.com/jobs?q="+job+"&l"
# print(url)
response = requests.get(url)
soup = bs(response.text,'html.parser')
# print(soup)




