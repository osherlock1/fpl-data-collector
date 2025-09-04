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

        #Input Parameters
        player_count = input("Input # of players: ") #Number of players graphed
        in_position = input("Input Player Position (FWD, MID, DEF, GKP): ")
        query_by = input("""Choose the stat to query players by: now_cost, total_points, form, ep_next, selected_by_percent,
                      minutes, goals_scored, assists, clean_sheets, goals_conceded, bonus, bps, chance_of_playing_next_round""")
        order_by = input("Order by: (DESC, ACS)") 
        in_x = input("""Input X axis statistic: (now_cost, total_points, form, ep_next, selected_by_percent,
                      minutes, goals_scored, assists, clean_sheets, goals_conceded, bonus, bps, chance_of_playing_next_round): """) 
        in_y = input("""Input Y axis statistic: (now_cost, total_points, form, ep_next, selected_by_percent,
                      minutes, goals_scored, assists, clean_sheets, goals_conceded, bonus, bps, chance_of_playing_next_round): """) 
        

        #Dictionary to map position to numerical values stored in db
        positions = ["FWD", "MID", "DEF", "GKP"]
        if in_position not in positions:
            final_pos = None #If None = All players
        else:
            pos_dict = {"MID" : 3, "FWD" : 4, "DEF" : 2, "GKP" : 1}
            final_pos = pos_dict[in_position]

        #Query Top Players Based on inputs
        top_players = db_manager.get_top_players(final_pos, player_count, query_by, order_by)



        desired_keys = ["web_name", in_x, in_y]

        for player in top_players:
            for key in desired_keys:
                print(f"{key}: {player[key]}")
            print("---")


        price = []
        points = []
        labels = []
        for player in top_players:
            price.append(int(player[in_x]) / 10)
            points.append(player[in_y])
            labels.append(player["web_name"])
        
        plt_mng.plot_scatter(x = price , y = points, labels = labels, xlabel=in_x, ylabel = in_y, title= (f"{in_y} vs. {in_x}"))

                
                


if __name__ == "__main__":
    main()