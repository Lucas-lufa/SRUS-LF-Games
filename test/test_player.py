import unittest

from app.player import Player

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

    def test_eq_true(self):
        self.player.score = 1
        self.playerOne.score = 1
        self.assertTrue(self.player == self.playerOne)

    def test_eq_false(self):
        self.player.score = 1
        self.playerOne.score = 2
        self.assertFalse(self.player == self.playerOne)    