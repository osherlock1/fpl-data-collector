import requests

base_url = "https://fantasy.premierleague.com/api/bootstrap-static/"

def get_info():
    response = requests.get(base_url)


    if response.status_code == 200:
        print("Data retrieved!")
        fpl_data = response.json()
        return fpl_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

fpl_info = get_info()
print(fpl_info.keys())

if fpl_info:
    player_list = fpl_info['elements']
    print(len(player_list))
    print(player_list)

for player in player_list[:30]:
    name = player['web_name']
    cost = player['now_cost'] / 10

if fpl_info:
    teams = fpl_info['teams']

    
for team in teams:
    print(team)


