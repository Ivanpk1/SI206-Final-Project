import requests
import json
import unittest
import os

API_KEY = "1e690ea0camshae97b1517e56281p1a8b47jsnf31096b1ea77"

def load_json(filename):
    try:
        with open(filename, "r") as file:
            json_data = json.load(file)
            print(f"FILE {filename} LOADED.")
            return json_data
    except FileNotFoundError:
        print(f"FILE {filename} NOT FOUND.")
        return {}

def write_json(dict, filename):
    try:
        with open(filename, "w") as file:
            json.dump(dict, file)
            print(f"DATA WRITTEN IN {filename}")
    except Exception as e:
        print(f"ERROR WRITING {filename}")

def get_nba_data(player):
    # parameters
    url = "api-nba-v1.p.rapidapi.com"
    params = {
        "apikey": API_KEY,
        "t": player
    }
    # convert response data to json
    response = requests.get(url, params=params)

