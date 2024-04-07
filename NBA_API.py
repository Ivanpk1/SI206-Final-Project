import requests

url = "https://api-nba-v1.p.rapidapi.com/players"

country = input("Enter country: ")

querystring = {"country": country}

headers = {
	"X-RapidAPI-Key": "1e690ea0camshae97b1517e56281p1a8b47jsnf31096b1ea77",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()
# print(data)

if data.get('results', 0) > 0:
    # gather names and country
    player_info = [(player['firstname'], player['lastname'], player['birth']['country']) for player in data['response']]

    for player in player_info:
        print(player)
else:
    print("No player was found")