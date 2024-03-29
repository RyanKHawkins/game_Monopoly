# Monopoly
# Author:  Ryan Hawkins
# Updated:  2019-11-08

# Goal:  Create a Python version of Monopoly.
"""
Gameplay

Start with $??.
Setup mulitplayer?
Setup computer?
Movement
    Roll two dice
    If rolled double, roll again
    If rolled double three times in a row, go to jail.
Purchase properties
Mortgage properties
Trade properties

Passing go


"""
"""
Layout each property
    Cost
    Position on board
    Overall value for trade limitations
    Groupings/Color
    Rent to earn for each level (0 to 4 houses, hotel)
    Relation/steps to each other
    
"""
"""
Community Chest

Create cards.

"""
"""
Special spots

Electric company
Waterworks
Railroads
Jail

"""
"""
Setup Player class:

Starting bank
"""
players = []


class Player:
    def __init__(self, name, money=1500):
        self.money = 1500
        self.name = name
        players.append(self.name)

    def __str__(self):
        return self.name

    def display_self(self):
        print(f"{self.name}")
        print(f"${self.money}")

    def set_players():
        players = []

        new_player = input("What's your name?\n")
        new_player = Player(new_player)
        players.append(new_player)
        return players

def main():

    Player.set_players()

main()
