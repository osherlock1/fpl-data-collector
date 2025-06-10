#Class to handle player data

class Player:
    def __init__(self, player_id: int, name: str, position_id: int, team_id: int):

        self.player_id = player_id
        self.name = name
        self.position_id = position_id
        self.team_id = team_id


    def display(self):
        print(f"Player Id: {self.player_id}")
        print(f"Name: {self.name}")
        print(f"Position_id: {self.position_id}")
        print(f"Team_id: {self.team_id}")

              


