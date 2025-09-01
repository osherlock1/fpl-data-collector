#Main file

from fpl_data_manager import FPLDataManager
from cli_config import cli_args

def main():

    args = cli_args() #get cli args
    databse_url = 'FPL_data.db'
    db_manager = FPLDataManager(databse_url)

    #Update Database
    if args.update_db:
        print("Updating database...")
        db_manager.update_teams_table()
        db_manager.update_position_table()
        db_manager.update_player_table()
        db_manager.update_daily_player()        
        print("Database update complete")

    #Run analysis and plot
    if args.analyze:

        top_players = db_manager.get_top_players(4, 30, "total_points", order_by="DESC")
        print(top_players)


if __name__ == "__main__":
    main()