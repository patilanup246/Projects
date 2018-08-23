'''
Created on Jun 7, 2018

@author: tasneem
'''
import sqlite3
import csv
def get_last_date():
    conn = sqlite3.connect('covers_database.db')
    cur = conn.execute("SELECT game_date from covers_data where ID = (SELECT max(ID) from covers_data)")
    data = cur.fetchall()

    if len(data) == 0 :
        return '2011-7-28'
    else:
        return data[0][0]

    conn.close()
    
    
def insert_data(dj_list):
    conn = sqlite3.connect('covers_database.db')
    
    for dj in dj_list:
        conn.execute("INSERT INTO covers_data (game_date, home_name, away_name, home_score, away_score, home_odds, away_odds, conference) \
                        VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(dj['game_date'], dj['home_name'], dj['away_name'], dj['home_score'], dj['away_score'], dj['home_odds'], dj['away_odds'], dj['conference']));
        conn.commit()
    conn.close()
    
def export_data():
    output_f = open('covers_export.csv','w',encoding='utf-8', newline='')
    wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
    wr.writerow(['Date of the game', 'Home Team Name', 'Away Team Name', 'Home Team Score', 'Away Team Score', 'Home Team Odds', 'Away Team Odds', 'Conference'])
    conn = sqlite3.connect('covers_database.db')
    cur = conn.execute("SELECT game_date, home_name, away_name, home_score, away_score, home_odds, away_odds, conference from covers_data")
    
    for row in cur:
        wr.writerow(row)
        
    conn.close()