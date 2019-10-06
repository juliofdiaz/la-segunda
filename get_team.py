import requests
import urllib.request
from util import format_time
from util import format_name
from bs4 import BeautifulSoup


def format_name(name_string):
    """ """
    return(name_string[:name_string.rfind(" ")],name_string[name_string.rfind(" "):])

def get_team(url):
    """ Gets list of players given team url """
    heads = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

    response = requests.get(url,headers=heads)
    soup = BeautifulSoup(response.text, "lxml")

    # Find player tags
    tab = soup.find_all("a", class_="spielprofil_tooltip")

    links = {}
    players = set()
    for i in tab:
        links[i.text] = i['href']
        name_item = i.findNext("td",{"class":"hide"})
        dob_item = i.findNext("td",{"class":"zentriert"})
        position_item =  dob_item.find_previous("tr")

        if name_item is not None and dob_item is not None:
            players.add((name_item.text, format_time(dob_item.text),position_item.text))
    
    data = []
    for a, b, c in players:
        data.append([format_name(a),b,c,links[a]])

    coach_item = soup.find_all("div", class_="container-hauptinfo")[0].findNext("a")
    coach = (format_name(coach_item.text), coach_item["href"])

    return((data, coach))

if __name__ == "__main__":
    url = "https://www.transfermarkt.co.uk/club-cienciano/startseite/verein/2729"
    team = get_team(url)

    players, coach =  team
    print(coach)
    for i in players:
        print(i)
