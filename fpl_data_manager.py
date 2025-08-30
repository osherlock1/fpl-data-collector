#Class to handle the SQL
import sqlite3
import requests
from datetime import date




class FPLDataManager:
    def __init__(self, db_path):

        self.fpl_api_url = "https://fantasy.premierleague.com/api/bootstrap-static/"
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

        #API call
        self.api_data = self._get_api_data()

        #Helper method to set up the database
        self._setup_database()



    #Runs the schema.sql to set up db file
    def _setup_database(self):

        print("Setting up database...")

        with open('schema.sql', 'r') as sql_file:
            schema_script = sql_file.read()


        self.cursor.executescript(schema_script)
        self.connection.commit()

        print("Database setup complete")


    #Helper function to connect to FPL API
    def _get_api_data(self):
        
        response = requests.get(self.fpl_api_url)

        if response.status_code == 200:
            print("API Data sucessfully retrieved!")
            data = response.json()
            return data
        else:
            print(f"Data retrieval failed \n Status code: {response.status_code}")


    #Function that gets the teams info and insets it to the teams table in db
    def update_teams_table(self):
        
        team_data = self.api_data.get('teams', [])
        if not team_data:
            print("No team data found")
            return
        
        for team in team_data:
            #Temp store data

            team_id = team['id']
            name = team['name']
            short_name = team['short_name']

            #INSERT it into table
            update_team_command = """INSERT OR IGNORE INTO teams (team_id, team_name, short_name) VALUES (?,?,?)"""

            self.cursor.execute(update_team_command, (team_id, name, short_name))
        self.connection.commit()
        print("Teams table populated succesffully")

    #Method to update the static information of the position data
    def update_position_table(self):

        position_data = self.api_data.get('element_types', [])
        if not position_data:
            print("No posiiton data found")
            return
        
        for position in position_data:

            position_id = position['id']
            name = position['singular_name']
            name_short = position['singular_name_short']

            update_position_command = """INSERT OR IGNORE into positions(position_id, position_name, short_name) VALUES (?,?,?)"""
            self.cursor.execute(update_position_command,(position_id, name, name_short))
        self.connection.commit()
        print("Position table populated succesfully")


    def update_player_table(self):

        player_api_data = self.api_data.get('elements',[])

        for player in player_api_data:
            web_name = player['web_name']
            player_id = player['id']
            position_id = player['element_type']
            team_id = player['team']

            update_player_command = """INSERT OR IGNORE INTO players(web_name, player_id, position_id, team_id) VALUES (?,?,?,?)"""
            self.cursor.execute(update_player_command,(web_name, player_id, position_id, team_id))
        
        self.connection.commit()
        print("Player data updated sucesfully!")

    def update_daily_player(self):

        player_api_data = self.api_data.get('elements', [])
        today = date.today()
        for player in player_api_data:
            player_id = player['id']
            log_date = today.isoformat()
            
            now_cost = player['now_cost']
            total_points = player['total_points']
            form = player['form']
            ep_next = player['ep_next']
            selected_by_percent = player['selected_by_percent']

            minutes = player['minutes']
            goals_scored = player['goals_scored']
            assists = player['assists']
            clean_sheets = player['clean_sheets']
            goals_conceded = player['goals_conceded']
            bonus = player['bonus']
            bps = player['bps']

            chance_of_playing_next_round = player['chance_of_playing_next_round']
            status = player['status']

            update_daily_stats_command = """INSERT OR IGNORE INTO player_daily_stats(
            player_id,
            log_date,
            
            now_cost,
            total_points,
            form,
            ep_next,
            selected_by_percent,
            
            minutes,
            goals_scored,
            assists,
            clean_sheets,
            goals_conceded,
            bonus,
            bps,
            
            chance_of_playing_next_round,
            status) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

            self.cursor.execute(update_daily_stats_command, (
                player_id, log_date, now_cost, total_points, form, ep_next, selected_by_percent,
                minutes, goals_scored, assists, clean_sheets, goals_conceded, bonus, bps,
                chance_of_playing_next_round, status
            ))
        self.connection.commit()
        print("Player Daily Log Updated")

    #TODO:FIGURE OUT HOW TO PROPERLY WORK THIS HELPER METHOD
    #helper function for query
    def _query(self, sql:str, params: tuple = ()) -> list:
        try:
            self.cursor.execute(sql, params)
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"Database query error: {e}")
            return []
        
    #TODO: FINISH THE GET_TOP_PLAYERS FUNCTION NEEED TO WORK ON HELPER METHODS
    def get_top_players(self, position, limit: int = 20, target_stat, order_by):
        where = "WHERE position = ?" if position else ""
        params = (position,) if position else ()
        rows = self._query()

        

    



