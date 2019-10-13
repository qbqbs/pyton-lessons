import requests
from bs4 import BeautifulSoup

def temp(html):
    return html.find("span", {"class":"temp__value"}).text 
def condition(html):    
    return html.find("div", {"class":"link__condition day-anchor i-bem"}).text
url = "https://yandex.ru/pogoda/nizhny-novgorod"
response = requests.get(url)
html = BeautifulSoup(response.content, "lxml")
#print(response.content)
print(temp(html))
print(condition(html))

hours = 3

sunset = 18
sunrise = 6

if hours >= sunrise and hours < sunset:
    print("На улице солнце")