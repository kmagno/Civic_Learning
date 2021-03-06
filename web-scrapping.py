import requests
from bs4 import BeautifulSoup
import jsontourl as geturl

filter = "public health"
name = "James Arciero"
house = "lower"
url = geturl.get_names(name, house)
page = requests.get(url,verify=False)
soup = BeautifulSoup(page.content, 'html.parser')
id_filter = soup.find(id="background")
# filter based on classes
bills = id_filter.find_all(class_="sponsoredBillTitle")
party_type = id_filter.find_all(class_="subTitle")
email_id =  id_filter.find_all(class_="repEmail text-center-on-xs")
phone_no =  id_filter.find_all(class_="col-xs-12 col-md-9")


print(len(bills))
print(party_type[0].get_text().strip())
print(email_id[0].get_text().strip())
print(phone_no[0].get_text().strip())
for i in range(len(bills)):
    text_part = bills[i].get_text().strip()
    if filter in text_part:
        print(text_part)
        print("---------------------------------------")
