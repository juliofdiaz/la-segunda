import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from datetime import datetime
import re

def get_actual_ref_score(score_string):
    return re.split(r'\s|\)', score_string)[3]

def tuple_from_name(name_string):
    temp = name_string.split(", ")
    if len(temp)<2:
        return("","")
    else:
        return (temp[1],temp[0])

def date_list_from_string(date_string):
    temp = date_string.split(" ")[1].split("/")
    return [int(temp[2]),int(temp[1]),int(temp[0])]

def time_list_from_string(time_string):
    temp = time_string.split(":")
    return [int(temp[0]),int(temp[1])]

def formation_from_string(formation_string):
    return re.split(r'\(|\)',formation_string)[1]

def team_from_string(formation_string):
    return formation_string.split(" (")[0]

def is_player_complete(player):
    
    return 

url = 'https://docs.google.com/spreadsheets/d/1Yhosll0nBhKZ-92XaEq-eTDLGZFXA1gJGfVWdYlDca4/pub'

#url = 'https://docs.google.com/spreadsheets/d/1dn6bsJ6cGA8bAXsPLjWBbDqc8yGYAml0zdt83TZnHCo/pub'

#url = 'https://docs.google.com/spreadsheets/d/1cfZ-F7vA0_Agi7piiDIaxkVVZiyXBlcv8MSJJBZIGv0/pub'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
#for i in soup.find('div', {"id":"doc-title"}).children:
#    print(i.text)

title = [i for i in soup.find("div",{"id":"doc-title"}).children][0]
print(title.text)

stadium_item = soup.find(text="EST").findNext("td")
stadium = stadium_item.text

score_one_item = stadium_item.findNext("td",{"class":"s4"})
score_one = score_one_item.text

ref_score_item = score_one_item.findNext("td") 
ref_score = get_actual_ref_score(ref_score_item.text)

score_two_item = ref_score_item.findNext("td",{"class":"s6"})
score_two = score_two_item.text

city_item = soup.find(text="CIU").findNext("td")
city = city_item.text

ref_item = soup.find(text="ÁRB").findNext("td")
ref = tuple_from_name(ref_item.text)

date_item = soup.find(text="FEC").findNext("td")
date = date_list_from_string(date_item.text)

ref_aa1_item = soup.find(text="AA1").findNext("td")
ref_aa1 = tuple_from_name(ref_aa1_item.text)

time_item = soup.find(text="HOR").findNext("td")
time = time_list_from_string(time_item.text)
when = datetime(date[0],date[1],date[2],time[0],time[1])

ref_aa2_item = soup.find(text="AA2").findNext("td")
ref_aa2 = tuple_from_name(ref_aa2_item.text)

aux_item = soup.find(text="AUX").findNext("td")
aux = tuple_from_name(aux_item.text)
print(aux)
formation_one_item = aux_item.findNext("td")
formation_one = formation_from_string(formation_one_item.text)
team_one = team_from_string(formation_one_item.text)

formation_two_item = formation_one_item.findNext("td")
formation_two = formation_from_string(formation_two_item.text)
team_two = team_from_string(formation_two_item.text)

previous_temp = formation_two_item.findNext("tr")

start_one = []
start_two = []
for i in range(1,12):
    temp_row = previous_temp.findNext("tr")
    
    player_one_number_item = temp_row.findNext("td")
    player_one_name_item = player_one_number_item.findNext("td")
    player_one_yellow1_item = player_one_name_item.findNext("td")
    player_one_yellow2_item = player_one_yellow1_item.findNext("td")
    player_one_red_item = player_one_yellow2_item.findNext("td")
    player_one_score_item = player_one_red_item.findNext("td")
    
    player_one = {}
    player_one["number"] = player_one_number_item.text
    player_one["name"] = tuple_from_name(player_one_name_item.text)
    player_one["yellow1"] = player_one_yellow1_item.text
    player_one["yellow2"] = player_one_yellow2_item.text
    player_one["red"] = player_one_red_item.text
    player_one["score"] = player_one_score_item.text
    start_one.append(player_one)

    player_two_number_item = player_one_score_item.findNext("td")
    player_two_name_item = player_two_number_item.findNext("td")
    player_two_yellow1_item = player_two_name_item.findNext("td")
    player_two_yellow2_item = player_two_yellow1_item.findNext("td")
    player_two_red_item = player_two_yellow2_item.findNext("td")
    player_two_score_item = player_two_red_item.findNext("td")

    player_two = {}
    player_two["number"] = player_two_number_item.text
    player_two["name"] = tuple_from_name(player_two_name_item.text)
    player_two["yellow1"] = player_two_yellow1_item.text
    player_two["yellow2"] = player_two_yellow2_item.text
    player_two["red"] = player_two_red_item.text
    player_two["score"] = player_two_score_item.text
    start_two.append(player_two)

    previous_temp = temp_row


bench_one = []
bench_two = []
while previous_temp.findNext("tr").findNext("td").text!="DT":
    temp_row = previous_temp.findNext("tr")

    player_one_number_item = temp_row.findNext("td")
    player_one_name_item = player_one_number_item.findNext("td")
    player_one_yellow1_item = player_one_name_item.findNext("td")
    player_one_yellow2_item = player_one_yellow1_item.findNext("td")
    player_one_red_item = player_one_yellow2_item.findNext("td")
    player_one_score_item = player_one_red_item.findNext("td")

    player_one = {}
    player_one["number"] = player_one_number_item.text
    player_one["name"] = tuple_from_name(player_one_name_item.text)
    player_one["yellow1"] = player_one_yellow1_item.text
    player_one["yellow2"] = player_one_yellow2_item.text
    player_one["red"] = player_one_red_item.text
    player_one["score"] = player_one_score_item.text
    bench_one.append(player_one)

    player_two_number_item = player_one_score_item.findNext("td")
    player_two_name_item = player_two_number_item.findNext("td")
    player_two_yellow1_item = player_two_name_item.findNext("td")
    player_two_yellow2_item = player_two_yellow1_item.findNext("td")
    player_two_red_item = player_two_yellow2_item.findNext("td")
    player_two_score_item = player_two_red_item.findNext("td")

    player_two = {}
    player_two["number"] = player_two_number_item.text
    player_two["name"] = tuple_from_name(player_two_name_item.text)
    player_two["yellow1"] = player_two_yellow1_item.text
    player_two["yellow2"] = player_two_yellow2_item.text
    player_two["red"] = player_two_red_item.text
    player_two["score"] = player_two_score_item.text    
    bench_two.append(player_two)

    previous_temp = temp_row


coach_one_item = previous_temp.findNext(text="DT").findNext("td")
coach_one = tuple_from_name(coach_one_item.text)

coach_two_item = coach_one_item.findNext(text="DT").findNext("td")
coach_two = tuple_from_name(coach_two_item.text)


previous_row = previous_temp.findNext(text="MIN")

subs_one = []
subs_two = []
for i in range(1,4):
    temp_row = previous_row.findNext("tr")

    min_one_item = temp_row.findNext("td")
    in_one_item = min_one_item.findNext("td")
    out_one_item = in_one_item.findNext("td")

    sub_one = {}
    sub_one["min"] = min_one_item.text
    sub_one["in"] = tuple_from_name(in_one_item.text)
    sub_one["out"] = tuple_from_name(out_one_item.text)
    subs_one.append(sub_one)

    min_two_item = out_one_item.findNext("td")
    in_two_item = min_two_item.findNext("td")
    out_two_item = in_two_item.findNext("td")
    
    sub_two = {}
    sub_two["min"] = min_two_item.text
    sub_two["in"] = tuple_from_name(in_two_item.text)
    sub_two["out"] = tuple_from_name(out_two_item.text)
    subs_two.append(sub_two)

    previous_row = temp_row

previous_row = previous_temp.findNext(text="Anotador")


goals_one = []
goals_two = []
while previous_row.findNext("tr").findNext("td").findNext("td").text!="Capitán":
#while previous_row.findNext("tr").findNext("td")["class"][0]!="s38":
#    print(previous_row.findNext("tr").findNext("td")["class"])
    temp_row = previous_row.findNext("tr")

    min_one_item = temp_row.findNext("td")
    player_one_item = min_one_item.findNext("td")
    body_one_item = player_one_item.findNext("td")
    type_one_item = body_one_item.findNext("td")

    goal_one = {}
    goal_one["min"] = min_one_item.text
    goal_one["player"] = player_one_item.text 
    goal_one["body"] = body_one_item.text
    goal_one["type"] = type_one_item.text
    goals_one.append(goal_one)

    min_two_item = type_one_item.findNext("td")
    player_two_item = min_two_item.findNext("td")
    body_two_item = player_two_item.findNext("td")
    type_two_item = body_two_item.findNext("td")
#    print(body_two_item.findNext("td"))

    goal_two = {}
    goal_two["min"] = min_two_item.text 
    goal_two["player"] = player_two_item.text
    goal_two["body"] = body_two_item.text
    goal_two["type"] = type_two_item.text
    goals_two.append(goal_two)
    
    previous_row = temp_row





print(stadium)

print(score_one)

print(ref_score)

print(score_two)

print(city)

print(ref)
 
print(ref_aa1)

print(when)

print(ref_aa2) 

print(aux)
 
print(formation_one)
 
print(team_one)
 
print(formation_two)

print(team_two)






print("start")
print(start_one)
print(start_two)

print(bench_one)
print(bench_two)

print(coach_one)
print(coach_two)

print("subs")
print(subs_one)
print(subs_two)

print(goals_one)
print(goals_two)

