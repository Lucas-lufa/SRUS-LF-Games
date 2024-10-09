import unittest

from app.player import Player
from app.player_list import Player_List

class Test_Player(unittest.TestCase):
    # setup 

    def setUp(self) -> None:
        self.player = Player(_uid="1", _name="Luke")
        self.playerOne = Player(_uid="2", _name="John")

    def test_initialisation(self):

        self.assertEqual(self.player._uid, "1")
        self.assertEqual(self.player._name, "Luke")

    def test_uid_property(self):
        self.assertEqual(self.player.uid, "1")

    def test_name_property(self):
        self.assertEqual(self.player.name, "Luke")

    def test_verify_password_None(self):
        self.assertFalse(self.player.verify_password(''))

    def test_add_password(self):
        self.player.add_password('password')
        self.assertIsNotNone(self.player._password_hash)

    def test_verify_password_false(self):
        self.player.add_password('password')
        self.assertFalse(self.player.verify_password('1'))

    def test_verify_password_true(self):
        self.player.add_password('password')
        self.assertTrue(self.player.verify_password('password'))

    def test_lt_true(self):
        self.player.score = 1
        self.playerOne.score = 2
        self.assertTrue(self.player < self.playerOne)

    def test_lt_false(self):
        self.player.score = 2
        self.playerOne.score = 1
        self.assertFalse(self.player < self.playerOne)

    def test_gt_true(self):
        self.player.score = 1
        self.playerOne.score = 2
        self.assertTrue(self.player < self.playerOne)

    def test_gt_false(self):
        self.player.score = 2
        self.playerOne.score = 1
        self.assertFalse(self.player < self.playerOne)

    def test_eq_true(self):
        self.player.score = 1
        self.playerOne.score = 1
        self.assertTrue(self.player == self.playerOne)

    def test_eq_false(self):
        self.player.score = 1
        self.playerOne.score = 2
        self.assertFalse(self.player == self.playerOne)

    def test_quicksort(self):
        player0 = Player("1", "Luke")
        player1 = Player("2","John" )
        player2 = Player("3","Fad")
        player3 = Player("4", "Kule")
        player4 = Player("5", "Ohnj")
        player5 = Player("6", "Dda")

        player0.score = 1
        player1.score = 2
        player2.score = 3
        player3.score = 4
        player4.score = 5
        player5.score = 6

        player_list = Player_List()

        player_list.insert_first(player0)
        player_list.insert_first(player1)
        player_list.insert_first(player2)
        player_list.insert_first(player3)
        player_list.insert_first(player4)
        player_list.insert_first(player5)
        sorted_players = Player.make_list(player_list)        

        player_list = Player_List()

        player_list.insert_first(player2)
        player_list.insert_first(player5)
        player_list.insert_first(player1)
        player_list.insert_first(player4)
        player_list.insert_first(player0)
        player_list.insert_first(player3)
        players = Player.make_list(player_list)

        Player.quick_sort(players, 0, len(players))
        self.assertTrue(sorted_players == players)

    