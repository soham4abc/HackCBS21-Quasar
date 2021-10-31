# This will not run on online IDE
import requests
from bs4 import BeautifulSoup

URL = "https://pharmeasy.in/search/all?name="
query = input("Enter Search Details : ")
URL = URL + query
r = requests.get(URL)

soup = BeautifulSoup(
    r.content, "html5lib"
)  # If this line causes an error, run 'pip install html5lib' or install html5lib
body = soup.find("body")
# print(soup.prettify())
i = 0
url_new = ""
for box in body.findAll("div", {"role": "menuitem"}):
    if i >= 1:
        break
    temp = box.find("a", {"class": "_2tdEn _1pXi6 _3o0NT _1NxW8 iJm6I"}).get("href")
    url_new = "https://pharmeasy.in" + temp
    print(url_new)
    i = i + 1


rnew = requests.get(url_new)
soupnew = BeautifulSoup(rnew.content, "html5lib")
bodynew = soupnew.find("body")
# print(bodynew.prettify())
for details in bodynew.findAll("div", {"class": "_2q0Km _31Aqa"}):
    # print(details.id)
    # print(details.get_text())
    # print(details)

    # Heading
    print(details.find("h2", {"class": "_1nIFK"}).get_text())

    # Inside
    print(details.find("div", {"class": "_1ZIK6"}).get_text())

    print("\n")
    # temp = details.find("_1ZIK6").getText()
    # print(temp)
    # print("\n\n")
