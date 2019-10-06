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

    info = soup.find_all("span", class_="dataItem")
    cob = info[1].findNext("span").text.strip()
    coc = info[2].findNext("span").text.strip()
    try:
        height = format_height(info[3].findNext("span").text.strip())
    except:
        height = -1

    try:
        foot = soup.find_all(string=re.compile("Foot:"))[0].findNext("td").text
    except:
        foot = "unknown"

    return [cob, coc, height, foot, transfers]


url = "https://www.transfermarkt.co.uk/jorge-molina/profil/spieler/94447"
url = "https://www.transfermarkt.co.uk/daniel-prieto/profil/spieler/217130"
url = "https://www.transfermarkt.co.uk/javier-salazar/profil/spieler/94872"
if __name__ == "__main__":
    player_info = get_player_info(url)

    print(player_info)
