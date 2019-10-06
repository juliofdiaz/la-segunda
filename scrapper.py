import time

from get_team import get_team as gt
from get_coach_info import get_coach_info as gc
from get_player_info import get_player_info as gp

from insert_into_positions import check_insert_into_positions as ciip

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
    print(player_name)
    print(player_dob)
    print(player_pos)
    ciip(player_pos)
    print("")

#    player = gp("https://www.transfermarkt.co.uk"+player_link)
#    print(player)

#    time.sleep(2)
#    break