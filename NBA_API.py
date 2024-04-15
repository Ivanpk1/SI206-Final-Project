import requests
import sqlite3

def create_table():
    """
    Create table

    Args: none

    Returns: none
    """
    conn = sqlite3.connect("countries.db")
    curr = conn.cursor()
    curr.execute('''CREATE TABLE IF NOT EXISTS NBA (
                        id INTEGER PRIMARY KEY,
                        firstname TEXT,
                        lastname TEXT,
                        country_id INTEGER
                    )''')
    conn.commit()
    conn.close()

def insert_players(player_info):
    """
    Insert player info into the table

    Args: player_info (tuple), first name, last name, country

    Returns: none
    """
    conn = sqlite3.connect("countries.db")
    curr = conn.cursor()
    for player in player_info:
        curr.execute("SELECT id FROM Countries WHERE Country = ?", (player[2],))
        country_id = curr.fetchone()
        if country_id:
            curr.execute("INSERT INTO NBA (firstname, lastname, country_id) VALUES (?, ?, ?)", (player[0], player[1], country_id[0]))
    conn.commit()
    conn.close()

def get_players():
    """
    Retrieve NBA players from a specific country from the API

    Args: country (str), country of origin

    Returns: none
    """
    url = "http://api.balldontlie.io/v1/players"
    headers = {
        "Authorization": "0fab7ce8-dd2f-403b-b6fa-4ab027f7d18e",
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)

    # gather names and country
    for player in data["data"]:
        player_info= [(player["first_name"], player["last_name"], player["country"])]
    print(player_info)
    # print(type(player_info))
    count = len(player_info)   
    print(count)  

    # print(f"{country} has {count} players in the NBA.")
    return player_info

# example
create_table()

def main():
    players_list = get_players()
    insert_players(players_list)

main()



