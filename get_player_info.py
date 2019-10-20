import requests
import urllib.request
from bs4 import BeautifulSoup
from util import format_time
from util import format_height
import re

def  get_player_info(url):
    heads = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

    response = requests.get(url,headers=heads)
    soup = BeautifulSoup(response.text, "lxml")

    # Find player tags
    tab = soup.find_all("tr", class_="zeile-transfer")

    transfers = []
    for i in tab:
        season_item = i.findNext("td", class_="zentriert")
        date_item = season_item.findNext("td", class_="zentriert")
        out_team_item = date_item.findNext("td", class_="hauptlink no-border-links hide-for-small vereinsname")
        in_team_item = out_team_item.findNext("td", class_="hauptlink no-border-links hide-for-small vereinsname")
        transfers.append([season_item.text,format_time(date_item.text),out_team_item.text.strip(),in_team_item.text.strip()])

    try:
        name_ob = soup.find_all("th", string=re.compile("Name in home country:"))[0].findNext("td").text
    except:
        name_ob = ""

    try:
        city_item = soup.find_all("th", string=re.compile("Place of birth:"))[0]
        country_ob= city_item.findNext("img")["title"]
        city_ob = city_item.findNext("span").text.strip()
    except:
        city_ob, country_ob = "unknown","unknown"

    citizen_holder = soup.find_all("th", string=re.compile("Citizenship:"))[0].find_next_siblings()
    citizen_items = citizen_holder[0].find_all("img", recursive=False)
    citizen = []
    for i in citizen_items:
        citizen.append(i['title'])

    try:
        height = format_height(soup.find_all("th", string=re.compile("Height:"))[0].findNext("td").text)
    except:
        height = -1

    try:
        foot = soup.find_all("th", string=re.compile("Foot:"))[0].findNext("td").text
    except:
        foot = "unknown"

    return [name_ob, (city_ob,country_ob), citizen, height, foot, transfers]

url = "https://www.transfermarkt.co.uk/kleiber-palomino/profil/spieler/520959"
#url = "https://www.transfermarkt.co.uk/jorge-molina/profil/spieler/94447"
#url = "https://www.transfermarkt.co.uk/daniel-prieto/profil/spieler/217130"
#url = "https://www.transfermarkt.co.uk/javier-salazar/profil/spieler/94872"
if __name__ == "__main__":
    player_info = get_player_info(url)

    print(player_info)
