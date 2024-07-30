import unittest

from app.player import Player

class Test_Player(unittest.TestCase):
    # setup 

    def setUp(self) -> None:
        self.player = Player(_uid="1", _name="Luke")

    def test_initilisation(self):

        self.assertEqual(self.player._uid, "1")
        self.assertEqual(self.player._name, "Luke")

    def test_uid_property(self):
        self.assertEqual(self.player.uid, "1")

    def test_name_property(self):
        self.assertEqual(self.player.name, "Luke")

