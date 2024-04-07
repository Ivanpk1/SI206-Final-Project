import requests

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
country = input("Enter country: ")
get_players_by_country(country)
