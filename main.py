






# install all dependecies 
import requests
from bs4 import BeautifulSoup as bs

# inspecting indeed.com to get a overview 



job="python+developer"

# url = "https://in.indeed.com/jobs?q="+job+"&l"
url = "https://in.indeed.com/"


# print(url)
response = requests.get(url)
print(response)
soup = bs(response.text,'html.parser')
print(soup)


# data=""
# for item in soup.find_all("a",class_="jcs-JobTitle css-jspxzf eu4oa1w0"):
#     print(item)
#     data=data+item.get_text()

# print(data)
