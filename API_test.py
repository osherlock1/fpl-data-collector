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

#What I need for the player table

#Players -> 'elements'
""""
chance_of_playing_next_round
chance_of_playing_this_round
code
dreamteam_count (# of times in best XI)
element_type (position)
ep_next (expected points from FPL algorithm)
ep_this (expected points this round from FPL)
event_points (most recent gw points)
form
id
in_dreamteam
now_cost
points_per_game
selected_by_percent
status (injury status)
team
team_code
total_points
transfers_in
transfers_in_event
transfers_out
transfers_out_event
value_form
value_season
web_name (name)
minutes
goals_scored
assists
clean_sheets
goals_conceded
own_goals
penalties_saved
penalties_missed
yellow_cards
red_cards
saves
bonus (bonus points)
bps (bonus point scoring system)
influence
creativity
threat
ict_index
starts
expected_goals
expected_assists
expected_goal_involvements
expected_goals_conceded
influence_rank
influence_rank_type
creativity_rank
creativity_rank_type
threat_rank
threat_rank_type
ict_index_rank
ict_index_rank_type
corners_and_indirect_freekicks_order
corners_and_indirect_freekicks_text
direct_freekicks_order
penalties_order
expected_goals_per_90
saves_per_90
expected_assists_per_90
expected_goal_involvements_per_90
expected_goals_conceded_per_90
goals_conceded_per_90
now_cost_rank
now_cost_rank_type
form_rank
form_rank_type
points_per_game_rank
points_per_game_rank_type
selected_rank
selected_rank_type
starts_per_90
clean_sheets_per_90
"""

