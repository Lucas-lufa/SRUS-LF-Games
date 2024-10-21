import unittest

from app.player_bst import PlayerBST
from app.player import Player

class Test_Player_bst(unittest.TestCase):

    #setup

    def setUp(self) -> None:
        self.player0 = Player(_uid="1", _name="Luke")
        self.player1 = Player(_uid="2", _name="John" )
        self.player2 = Player(_uid="3", _name="Fad")
        self.player3 = Player(_uid="4", _name="Kule")
        self.player4 = Player(_uid="5", _name="Ohnj")
        self.player5 = Player(_uid="6", _name="Daf")
        
        self.bst = PlayerBST()

        # self.bst.insert(self.player2)
        # self.bst.insert(self.player3)
        # self.bst.insert(self.player5)
    
    def test_insert_left(self):
        self.bst.insert(self.player0)
        self.bst.insert(self.player1)

        self.assertEqual(self.bst._root._left.player , self.player1)


    def test_insert_right(self):
        self.bst.insert(self.player0)
        self.bst.insert(self.player4)
        
        self.assertEqual(self.bst._root._right.player , self.player4)

