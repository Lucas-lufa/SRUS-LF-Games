import unittest

from app.player_bst import PlayerBST
from app.player import Player

class Test_Player_bst:

    #setup

    def setup(self) -> None:
        self.player0 = Player("1", "Luke")
        self.player1 = Player("2","John" )
        self.player2 = Player("3","Fad")
        self.player3 = Player("4", "Kule")
        self.player4 = Player("5", "Ohnj")
        self.player5 = Player("6", "Dda")

        bst = PlayerBST()

    