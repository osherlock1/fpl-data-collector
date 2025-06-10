#Class to handle the daily logs of the players

class PlayerDailyStats:
    def __init__(self, player_data):

        """
        player_data is the library of an individual player from the API data
        """

        self.player_data = player_data

        #API data
        self.player_id = player_data['player_id']
