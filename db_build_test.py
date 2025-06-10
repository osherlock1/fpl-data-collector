#Script for testing the build of the db
import sqlite3


#Table1 Players: This table holds info of static info about the player
#Table2 player_data_log:  This table holds info of weekly stats for the players

#Table3 teams:  This table holds the name of all the teams and team ids



db_name = "FPL_data.db"


def build_db(db_name):
    connection = sqlite3.connect("FPL_data.db")
    cursor = connection.cursor()

    #Static Player Data store player data that never or rarely changes

    build_player_table = """CREATE TABLE IF NOT EXISTS players(
    player_id INTEGER PRIMARY KEY,
    web_name TEXT NOT NULL,
    position_id INTEGER NOT NULL,
    team_id INTEGER NOT NULL,
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (position_id) REFERENCES positions(position_id)
    )"""

    cursor.execute(build_player_table)


    #Time Series Player Data to store weekly/daily data TBD

    build_player_log = """CREATE TABLE IF NOT EXISTS player_data_log(
    log_id INTEGER PRIMARY KEY,
    player_id INTEGER NOT NULL,
    log_date TEXT NOT NULL,
    now_cost INTEGER NOT NULL,
    total_points INTEGER NOT NULL,
    points_per_game REAL NOT NULL,
    form REAL NOT NULL,
    ep_next REAL NOT NULL,
    ep_this REAL NOT NULL,
    event_points INTEGER NOT NULL,
    selected_by_percent REAL NOT NULL,
    transfers_in INTEGER NOT NULL,
    transfers_in_event INTEGER NOT NULL,
    transfers_out INTEGER NOT NULL,
    transfers_out_event INTEGER NOT NULL,
    value_form REAL NOT NULL,
    value_season REAL NOT NULL,
    minutes INTEGER NOT NULL,
    starts INTEGER NOT NULL,
    goals_scored INTEGER,
    assists INTEGER,
    clean_sheets INTEGER,
    own_goals INTEGER,
    penalties_saved INTEGER,
    penalties_missed INTEGER,
    yellow_cards INTEGER,
    red_cards INTEGER,
    saves INTEGER,
    bonus INTEGER,
    bps INTEGER,
    chance_of_playing_next_round INTEGER,
    chance_of_playing_this_round INTEGER,
    status TEXT,
    dreamteam_count INTEGER,
    in_dreamteam INTEGER,
    influence REAL,
    creativity REAL,
    threat REAL,
    ict_index REAL,
    influence_rank INTEGER,
    influence_rank_type INTEGER,
    creativity_rank INTEGER,
    threat_rank INTEGER,
    threat_rank_type INTEGER,
    expected_goals REAL,
    expected_assists REAL,
    expected_goal_involvements REAL,
    expected_goals_conceded REAL,
    corners_and_indirect_freekicks_order INTEGER,
    direct_freekicks_order INTEGER,
    penalties_order INTEGER,
    expected_goals_per_90 REAL,
    saves_per_90 REAL,
    expected_assists_per_90 REAL,
    expected_goal_involvements_per_90 REAL,
    expected_goals_conceded_per_90 REAL,
    goals_conceded_per_90 REAL,
    starts_per_90 REAL,
    clean_sheets_per_90 REAL,
    now_cost_rank INTEGER,
    now_cost_rank_type INTEGER,
    form_rank INTEGER,
    form_rank_type INTEGER,
    points_per_game_rank INTEGER,
    points_per_game_rank_type INTEGER,
    selected_rank INTEGER,
    selected_rank_type INTEGER,
    FOREIGN KEY (player_id) REFERENCES players (player_id)
    )"""

    cursor.execute(build_player_log)


    #Team table for storing team info/ team names
    build_team_table = """CREATE TABLE IF NOT EXISTS teams(
    team_id INTEGER PRIMARY KEY,
    team_name TEXT NOT NULL,
    short_name TEXT NOT NULL)"""

    cursor.execute(build_team_table)


    #Positions table for storing the text names of positions
    build_positions_table = """CREATE TABLE IF NOT EXISTS positions(
    position_id INTEGER PRIMARY KEY,
    position_name TEXT NOT NULL,
    short_name TEXT NOT NULL)"""

    cursor.execute(build_positions_table)


build_db(db_name)



