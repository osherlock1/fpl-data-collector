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


fpl_data = get_api_data(base_url)
          
player_data = fpl_data['elements']



all_players = []


for player in player_data:
     
     web_name = player['web_name']
     player_id = player['id']
     position_id = player['element_type']
     team_id = player['team']
     all_players.append(Player(player_id, web_name, position_id, team_id))
     #print(f"Sucessfully Created Player Class for {web_name}")


for player in all_players[:5]:
     print(f"Player name: {player.name} --- Player id: {player.player_id}")





def get_team_info(base_url):
     pass
