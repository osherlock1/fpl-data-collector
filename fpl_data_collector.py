#File designed to collected data from the public FPL API
import requests
from PlayerDailyStats import PlayerDailyStats
from player import Player
base_url = "https://fantasy.premierleague.com/api/bootstrap-static/"

def get_api_data(base_url):
    
     response = requests.get(base_url)

     if response.status_code == 200:
          print("Data sucessfully retrieved!")
          data = response.json()
          return data
     else:
          print(f"Data retrieval failed \n Status code: {response.status_code}")

def get_player_data(player_data):

    all_players = []

    for player in player_data:
        
        

        web_name = player['web_name']
        player_id = player['id']
        position_id = player['element_type']
        team_id = player['team']
        all_players.append(Player(player_id, web_name, position_id, team_id))
        #print(f"Sucessfully Created Player Class for {web_name}")
    
    return all_players


fpl_data = get_api_data(base_url)
          
player_data = fpl_data['elements']

player_list = get_player_data(player_data)






