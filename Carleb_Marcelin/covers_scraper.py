'''
Created on Jun 7, 2018

@author: tasneem
'''
import datetime
import requests
from pyquery import PyQuery
import database_connect
import json
MAIN_PAGE = 'https://www.covers.com/sports/MLB/matchups?selectedDate='

def get_today_date():
    today_date = datetime.datetime.now()
    return str(today_date.year)+'-'+str(today_date.month)+'-'+str(today_date.day)


def scrape_page(game_date):
    
    json_list = []
    
    r = requests.get(MAIN_PAGE+game_date)
    
    pq = PyQuery(r.text)
    
    for card in pq('.cmg_matchup_game_box'):
        try:
            json_obj = {}
            teams_names = pq(card)('.cmg_matchup_header_team_names').text().split(' at ')
            home_name   = teams_names[0]
            away_name   = teams_names[1]
            home_score  = pq(card)('.cmg_matchup_line_score tr:nth-of-type(1) .cmg_matchup_line_score_total').text()
            away_score  = pq(card)('.cmg_matchup_line_score tr:nth-of-type(2) .cmg_matchup_line_score_total').text()
            ths = []
            for th in pq(card)('.cmg_matchup_line_score tr:nth-of-type(1) th'):
                ths.append(th.text)
            inde = ths.index('ML')
            home_odds   = pq(card)('.cmg_matchup_line_score tr:nth-of-type(1) td:nth-of-type({})'.format(inde+1)).text()
            away_odds   = pq(card)('.cmg_matchup_line_score tr:nth-of-type(2) td:nth-of-type({})'.format(inde+1)).text()
            conference  = pq(card)('.cmg_matchup_header_conference').text()
            
            json_obj['game_date']   = game_date
            json_obj['home_name']   = home_name
            json_obj['away_name']   = away_name
            json_obj['home_score']  = home_score
            json_obj['away_score']  = away_score
            json_obj['home_odds']   = home_odds
            json_obj['away_odds']   = away_odds
            json_obj['conference']  = conference
            if not 'Spring Training' in conference:
                json_list.append (json_obj)
                #print (json.dumps(json_obj))
        except Exception as e:
            print (e)
    database_connect.insert_data(json_list)

        

last_date = database_connect.get_last_date()
today_date = get_today_date()
new_date = datetime.datetime(int(last_date.split('-')[0]),int(last_date.split('-')[1]),int(last_date.split('-')[2]))

while True:
     
    if last_date == today_date:
        break
    
    new_date += datetime.timedelta(days=1)
    
    new_date_string = str(new_date.year)+'-'+str(new_date.month)+'-'+str(new_date.day)
    print (new_date)

    
    
    if  new_date_string == get_today_date():
        break
    
    scrape_page(new_date_string)
database_connect.export_data()
# date = datetime.datetime(2003,7,29)
# for i in range(5): 
#     date += datetime.timedelta(days=1)
#     print(date.day)



    

    
