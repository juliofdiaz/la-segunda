import requests
import urllib.request
from bs4 import BeautifulSoup
from util import format_time

def  get_coach_info(url):
    heads = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

    response = requests.get(url,headers=heads)
    soup = BeautifulSoup(response.text, "lxml")

    dob_item = soup.find_all("th", string="Date of Birth:")[0].findNext("td")
    cob_item = soup.find_all("th", string="Citizenship:")[0].findNext("td")

    return [format_time(dob_item.text),cob_item.text.strip()]

    
if __name__ == "__main__":
    url = "https://www.transfermarkt.co.uk/marcelo-grioni/profil/trainer/45713"
    coach_info = get_coach_info(url)
    print(coach_info)
