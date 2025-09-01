#Main file

from fpl_data_manager import FPLDataManager
from cli_config import cli_args
from plotter import PlotManager


def main():

    args = cli_args() #get cli args
    databse_url = 'FPL_data.db'
    db_manager = FPLDataManager(databse_url)

    #plot manager instance
    plt_mng = PlotManager()

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

        top_players = db_manager.get_top_players(4, 100, "total_points", order_by="DESC")


        desired_keys = ["web_name", "total_points", "now_cost"]

        for player in top_players:
            for key in desired_keys:
                print(f"{key}: {player[key]}")
            print("---")


        price = []
        points = []
        labels = []
        for player in top_players:
            price.append(int(player["now_cost"]) / 10)
            points.append(player["total_points"])
            labels.append(player["web_name"])
        
        plt_mng.plot_scatter(x = price , y = points, labels = labels)

                
                


if __name__ == "__main__":
    main()