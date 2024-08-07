import unittest

from app.player import Player
from app.player_list import Player_List

class Test_Player_List(unittest.TestCase):

    #setup

    def setUp(self)-> None:
        """
        docstring
        """
        self.player = Player(_uid="1", _name="Luke")
        self.player_list = Player_List()

    def test_add_node_to_empty_list(self):
        """
        docstring
        """
        self.player_list.insert_first(self.player)
        self.assertEqual("1", self.player_list.head.key)

    def test_add_node_to_list(self):
        self.player = Player("2","John")
        self.player_list.insert_first(self.player)
        self.assertEqual("2", self.player_list.head.key)