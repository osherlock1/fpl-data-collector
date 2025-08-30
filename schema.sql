-- This file defines the complete database structure for the FPL project.
-- It is the single source of truth for the database schema and is used to
-- initialize a new, empty database.

-- Table 1: teams
-- Stores static information about each of the 20 Premier League teams.
CREATE TABLE IF NOT EXISTS teams (
    team_id INTEGER PRIMARY KEY,
    team_name TEXT NOT NULL,
    short_name TEXT NOT NULL
);

-- Table 2: positions
-- Stores the mapping from a position ID to its name (e.g., 2 -> 'Defender').
CREATE TABLE IF NOT EXISTS positions (
    position_id INTEGER PRIMARY KEY,
    position_name TEXT NOT NULL,
    short_name TEXT NOT NULL
);

-- Table 3: players
-- Stores static information for each player. This table links a player
-- to their team and position using Foreign Keys.
CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY,
    web_name TEXT NOT NULL,
    position_id INTEGER,
    team_id INTEGER,
    FOREIGN KEY (position_id) REFERENCES positions (position_id),
    FOREIGN KEY (team_id) REFERENCES teams (team_id)
);

-- Table 4: player_daily_stats
-- This is the main time-series table. A new row will be added here
-- for each player every day to log their changing stats.
CREATE TABLE IF NOT EXISTS player_daily_stats (
    log_id INTEGER PRIMARY KEY,
    player_id INTEGER NOT NULL,
    log_date TEXT NOT NULL,
    
    -- Key Fantasy Metrics
    now_cost INTEGER NOT NULL,
    total_points INTEGER NOT NULL,
    form REAL NOT NULL,
    ep_next REAL NOT NULL,
    selected_by_percent REAL NOT NULL,
    
    -- Performance Stats
    minutes INTEGER NOT NULL,
    goals_scored INTEGER NOT NULL,
    assists INTEGER NOT NULL,
    clean_sheets INTEGER NOT NULL,
    goals_conceded INTEGER NOT NULL,
    bonus INTEGER NOT NULL,
    bps INTEGER NOT NULL,
    
    -- Availability Stats
    chance_of_playing_next_round INTEGER,
    status TEXT NOT NULL,
    
    FOREIGN KEY (player_id) REFERENCES players (player_id),
    UNIQUE (player_id, log_date)
);
