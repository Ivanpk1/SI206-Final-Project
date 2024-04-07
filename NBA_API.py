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
    curr.execute('''CREATE TABLE IF NOT EXISTS players (
                        id INTEGER PRIMARY KEY,
                        firstname TEXT,
                        lastname TEXT,
                        country TEXT
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
    cur = conn.cursor()
    cur.execute("INSERT INTO players (firstname, lastname, country) VALUES (?, ?, ?)", player_info)
    conn.commit()
    conn.close()

def get_players_by_country(country):
    """
    Retrieve NBA players from a specific country from the API

    Args: country (str), country of origin

    Returns: none
    """
    url = "https://api-nba-v1.p.rapidapi.com/players"
    querystring = {"country": country}
    headers = {
        "X-RapidAPI-Key": "1e690ea0camshae97b1517e56281p1a8b47jsnf31096b1ea77",
        "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    if data.get("results", 0) > 0:
        # gather names and country
        player_info = [(player["firstname"], player["lastname"], player["birth"]["country"]) for player in data["response"]]
        count = len(player_info)

        for player in player_info:
            print(player)
    else:
        print("No player was found")

    print(f"{country} has {count} players in the NBA.")

# example
create_table()
country = input("Enter country: ")
get_players_by_country(country)
