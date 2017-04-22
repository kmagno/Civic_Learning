import requests
from bs4 import BeautifulSoup
import json

name = "education"
url = "https://www.boston.gov/departments/city-council/%s"%name
names = [];
page = requests.get(url,verify=False)
soup = BeautifulSoup(page.content, 'html.parser')
id_filter = soup.find(id="content")
# filter based on classes
all_members = id_filter.find_all(class_="person-profile-display-name")

for i in range(len(all_members)):
    text_part = all_members[i].get_text().strip()
    names.append(text_part)

data = {
   'name' : names
}

json_str = json.dumps(data)
print(json_str)
