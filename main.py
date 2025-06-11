#Main file

from fpl_data_manager import FPLDataManager


def main():
    
    database_url = 'FPL_data.db'

    db_manager = FPLDataManager(database_url)

    db_manager.update_teams_table()

    db_manager.update_position_table()

    db_manager.update_player_table()

    db_manager.update_daily_player()
    
if __name__ == "__main__":
    main()