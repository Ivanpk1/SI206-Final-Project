from bs4 import BeautifulSoup
import regex as re 
import requests
import os
import sqlite3


#maybe has to do with why the database is locked
def setupDatabase(filename):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + filename)
    cur = conn.cursor()
    return cur, conn

def populateDatabase(data, cur, conn):
    
    #creating tables if not exist
    cur.execute("CREATE TABLE IF NOT EXISTS Countries (id INTEGER PRIMARY KEY, Country TEXT UNIQUE, Population INTEGER)")
    
    #populating the data base with an id, the country name, and the population
    for i in range(len(data)):
        cur.execute("INSERT OR IGNORE INTO Countries (id, Country, Population) VALUES (?, ?, ?)", 
                    (i, data[i][0], data[i][1]))
        
    conn.commit()

def getData(soup):
    
    #type of what we are finding 
    tables = soup.find_all('tr')
    
    data = []
    for item in tables:        
        country = item.find('a')
        pop = item.find('td', style="font-weight: bold;") #population
            
        if country and pop:
            #using regex to substitute , with blanck spaces
            pop = re.sub(',', '', pop.text)
            pop = int(pop)
            data.append((country.text, pop))
    
    return data
        
        
def main():
    url = "https://www.worldometers.info/world-population/population-by-country/"
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    
    cur, conn = setupDatabase("countries.db")
    data = getData(soup)
    populateDatabase(data, cur, conn)
    
    conn.close()        
    
main()
    