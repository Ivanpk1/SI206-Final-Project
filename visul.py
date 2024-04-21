import matplotlib.pyplot as plt
import math
import os
import sqlite3

def calculations(conn, cur): #return 3 dictionaries         
    
    # getting country name and id together
    #    
    cur.execute("""
                SELECT country_id, COUNT(*) as count
                FROM Soccer
                GROUP BY country_id
                ORDER BY count DESC;
                """)
    soccer_counts = cur.fetchall()
    print(soccer_counts)
    
    cur.execute("""
                SELECT country_id, COUNT(*) as count
                FROM Soccer
                GROUP BY country_id
                ORDER BY count DESC;
                """)
    soccer_counts = cur.fetchall()
    print(soccer_counts)
    
    cur.execute("""
                """)


def visual_1():
    # bar chart    
    
    pass

def visual_2():
    # histogram   Soccer countries
    
    pass

def visual_3():
    # pie chart NBA
    
    pass

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + 'countries.db')
    cur = conn.cursor()
    calculations(conn, cur)
    conn.commit()
    conn.close()

main()