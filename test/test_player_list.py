import unittest

from app.player import Player
from app.player_list import Player_List

class Test_Player_List(unittest.TestCase):

    #setup

    def setUp(self)-> None:
        """
        docstring
        """
        self.player = Player("1", "Luke")
        self.player_list = Player_List()


    def test_add_node_to_empty_list_insert_first(self):
        """
        docstring
        """
        self.player_list.insert_first(self.player)
        self.assertEqual("1", self.player_list.head.key)

    def test_add_node_to_list_insert_first(self):
        player = Player("2","John")
        self.player_list.insert_first(self.player)
        self.player_list.insert_first(player)
        self.assertEqual("2", self.player_list.head.key)


    def test_add_node_to_empty_list_insert_last(self):
        """
        docstring
        """
        self.player_list = Player_List()
        player = Player("2","John")
        self.player_list.insert_last(player)
        self.assertEqual("2", self.player_list.head.key)
        self.assertEqual("2", self.player_list.tail.key)

    def test_add_node_to_list_insert_last(self):
        player = Player("2","John")
        self.player_list.insert_last(self.player)
        self.player_list.insert_last(player)
        self.assertEqual("1", self.player_list.head.key)
        self.assertEqual("2", self.player_list.tail.key)


    def test_delete_head(self):
        self.player_list.insert_first(self.player)
        player = Player("2","John")
        self.player_list.insert_first(player)
        self.player_list.delete_head()
        self.assertEqual(self.player, self.player_list._head.player)

    def test_delete_head_is_empty(self):
        pass

    def test_delete_head_one_node(self):
        self.player_list.delete_head()
        self.assertEqual(self.player_list.head, None)

    def test_delete_tail(self):
        self.player_list.insert_first(self.player)
        player = Player("2","John")
        self.player_list.insert_last(player)
        self.player_list.delete_tail()
        self.assertEqual("1", self.player_list.tail.key)

    def test_delete_tail_is_empty(self):
        pass

    def test_delete_tail_one_node(self):
        self.player_list.delete_head()
        self.assertEqual(self.player_list.head, None)

    def test_delete_key(self):
        self.player_list.insert_first(self.player)
        player = Player("2","John")
        self.player_list.insert_first(player)
        player = Player("3","Fad")
        self.player_list.insert_first(player)

        self.player_list.delete_key('3')

        self.assertEqual(self.player_list.head.key, '2' )
