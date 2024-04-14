import requests
import json
import time
import os
import sqlite3

path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path + "/" + 'countries.db')
cur = conn.cursor()

football_clubs = [
    # Bundesliga
    "Bayern_Munchen", "Borussia_Dortmund", "RB_Leipzig", "Borussia_Monchengladbach", 
    "Bayer_Leverkusen", "Eintracht_Frankfurt", "VfL_Wolfsburg", "Augsburg", 
    "TSG_Hoffenheim", "Hertha_Berlin", "FC_Koln", "SC_Freiburg", "Union_Berlin", 
    "FSV_Mainz_05", "VfB_Stuttgart", "Arminia_Bielefeld", "Schalke_04",
    # La Liga
    "Real_Madrid", "Barcelona", "Atletico_Madrid", "Sevilla", "Real_Sociedad", 
    "Villarreal", "Real_Betis", "Athletic_Bilbao", "Granada", "Valencia", 
    "Cadiz", "Levante", "Osasuna", "Getafe", "Huesca", "Real_Valladolid", 
    "Elche", "Eibar",
    # Ligue 1
    "Paris_Saint_Germain", "Marseille", "Lyon", "Monaco", "Lille", 
    "Montpellier", "Nice", "Rennes", "Reims", "Saint_Etienne", "Angers", "Brest", 
    "Metz", "Nantes", "Strasbourg", "Bordeaux", "Lorient", "Dijon", "Nimes",
    # Serie A
    "Juventus", "Inter_Milan", "AC_Milan", "Napoli", "Atalanta", "Roma", "Lazio", 
    "Sassuolo", "Verona", "Fiorentina", "Udinese", "Sampdoria", "Genoa", "Bologna", 
    "Spezia", "Cagliari", "Parma", "Torino", "Benevento", "Crotone",
    # English Premier League
    "Manchester_United", "Manchester_City", "Liverpool", "Chelsea", "Leicester_City", 
    "West_Ham_United", "Tottenham_Hotspur", "Everton", "Aston_Villa", "Arsenal", 
    "Leeds_United", "Wolves", "Crystal_Palace", "Southampton", 
    "Burnley", "Brighton_Hove_Albion", "Newcastle_United", "Fulham", 
    "West_Bromwich", "Sheffield_United"
]

# ids_list = []
# for team in football_clubs:
#     url = f'http://api.isportsapi.com/sport/football/team/search?api_key=LEF2p56y5YYXmVnw&name={team}'
#     response = requests.get(url)
#     json_string = response.content.decode('utf-8')
#     dictionary = json.loads(json_string)
#     if team == "Angers":
#         ids_list.append(dictionary['data'][3]['teamId'])
#     else:
#         ids_list.append(dictionary['data'][0]['teamId'])
#     time.sleep(5)
# print(ids_list)


ids_list = ['88', '99', '13201', '128', '165', '423', '149', '1135', '1078', '139', '490', '172', '1087', '162', '155', '90', '151', '82', '84', '109', '86', '106', '107', '96', '92', '121', '91', '143', '103', '94', '98', '3225', '123', '126', '131', '271', '211', '205', '197', '266', '351', '259', '251', '4957', '255', '1098', '306', '214', '263', '260', '208', '333', '320', '1744', '166', '152', '150', '1419', '154', '174', '182', '2960', '559', '176', '187', '179', '552', '185', '1390', '183', '189', '558', '1420', '554', '27', '26', '25', '24', '59', '62', '33', '31', '20', '19', '56', '52', '35', '30', '46', '60', '28', '29', '18', '51']

# player_data = {}
# for ids in ids_list:
#     url = f'http://api.isportsapi.com/sport/football/player?api_key=LEF2p56y5YYXmVnw&teamId={ids}'
#     response = requests.get(url)
#     json_string = response.content.decode('utf-8')
#     dictionary = json.loads(json_string)
#     print(dictionary)
#     for data in dictionary['data']:
#         player_data[data['name']] = data['country']
#     time.sleep(10)
#hifwhefih

cur.execute(
    "CREATE TABLE IF NOT EXISTS Soccer (id INTEGER PRIMARY KEY, name TEXT, country_id INTEGER)"
)
for player in player_data:
    cur.execute("SELECT id FROM Countries WHERE Country = ?", (player_data[player],))
    country_id = cur.fetchone()
    if country_id:
        cur.execute("INSERT INTO Soccer (name, country_id) VALUES (?, ?)", (player, country_id[0]))
conn.commit()
conn.close()