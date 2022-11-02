URL = 'https://www.pagesjaunes.fr/annuaire/altkirch-68/professionnels'

import csv
from bs4 import BeautifulSoup

with open("PagesJaunes.html") as file:
    contents  = file.read()

soup = BeautifulSoup(contents, "html.parser")
all_link_tags = soup.select(selector=".col-xs-12 a")

# field names
fields = ['NAME', 'LINK']

# data rows of csv file
rows = []

for tag in all_link_tags:
    dict={"NAME": "", "LINK": ""}
    dict["LINK"] = tag.get("href")
    dict["NAME"] = tag.getText()
    print(dict)
    rows.append(dict)


print(rows)

# name of csv file
filename = "prof_links.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames = fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(rows)
"""
#COOKIES FOR THE SITE
cookies = {
    "pjtmctxv1": "964a6917-daa9-4dea-cd23-8908a025d5c0-5290b39-31ce#2ce50dfc-a8f6-444e-b5fe-6622a697d3ba#WF7BC#N#b7674e9a-8846-4b66-b92f-378c84036d98#W2904#20221101#e64579c9f67437444a70a0d49cde06ef",
    "atuserid": "%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%220adb1753-74c1-4064-ac5c-b23d53d4e7a5%22%2C%22options%22%3A%7B%22end%22%3A%222023-12-03T13%3A31%3A11.875Z%22%2C%22path%22%3A%22%2F%22%7D%7D",
    "_gcl_au": "1.1.1903958525.1667309473",
    "pj_policy_cookie": "1",
    "atauthority": "%7B%22name%22%3A%22atauthority%22%2C%22val%22%3A%7B%22authority_name%22%3A%22default%22%2C%22visitor_mode%22%3A%22optin%22%7D%2C%22options%22%3A%7B%22end%22%3A%222023-12-03T13%3A32%3A10.497Z%22%2C%22path%22%3A%22%2F%22%7D%7D",
    "_cs_c": "1",
    "kameleoonVisitorCode": "9jzqco9yyf65o3c8",
    "atidvisitor": "%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-483323-%22%2C%22at%22%3A%22%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A12787200%2C%22end%22%3A12787200%7D%7D",
    "__cf_bm": ".7tzL4I1GeCqpvd.4013tzJAuOeyZ.fhNNZDAA6aalI-1667320559-0-AViJTdY7QLJbxvwWRT6dDxyq3/+hXbQ1Lm48hKl0tTNKWHrYUeaU7Ldsw6cfERuhzfHSRhbSJrlsZSyxHK1KzD9QOoh3ACTjTSkh+8fvwUaw",
    "_cs_id": "8a805708-85c9-a9d7-9fc9-12df3643ff8b.1667309530.3.1667320707.1667320553.1.1701473530571",
    "_cs_s": "4.5.0.1667322507315",
    "uuid": "952728e5533643a1a55dc36ce5b5406e",
    "OPTOUT": "0",
    "m-4": "1",
    "m-7": "1",
    "m-1": "1",
    "m-3": "1"
}


response = requests.get(url=URL, cookies=cookies)
print(response.content)
"""