import time

from get_team import get_team as gt
from get_coach_info import get_coach_info as gc
from get_player_info import get_player_info as gp

#from db_setup.insert_into_positions import check_insert_into_positions as cii_pos
#from db_setup.insert_into_cities import check_insert_into_cities as cii_city
from db_setup.insert_into_players import check_insert_into_players as cii_player

url = "https://www.transfermarkt.co.uk/club-cienciano/startseite/verein/2729"
url = "https://www.transfermarkt.co.uk/sport-loreto/startseite/verein/46663"
team = gt(url)

players, coach =  team
coach_name, coach_link = coach
coach_dob, coach_country = gc("https://www.transfermarkt.co.uk"+coach_link)

print("""coach_name:\t"""+str(coach_name)+"""\n"""
+"""coach_link:\t"""+coach_link+"""\n"""
+"""coach_dob:\t"""+coach_dob+"""\n"""
+"""coach_country:\t"""+coach_country+"""\n""")


for player_name,player_dob,player_pos,player_link in players:
    first_name, last_name = player_name
    print(player_dob)
    print(player_pos)


    name_ob, city_ob, citizenship, height, foot, transfers = gp("https://www.transfermarkt.co.uk"+player_link)

    print(cii_player((first_name,last_name,name_ob,city_ob,citizenship,player_dob,foot,height,player_pos,player_link)))

    time.sleep(2)
