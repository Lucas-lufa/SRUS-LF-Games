from argon2 import PasswordHasher
import argon2
import argon2.exceptions

from app.player_list import Player_List

class Player:
    """Holds the detail of the player
    """
    def __init__(self, _uid:str, _name:str) -> None:
        self._uid:str = _uid
        self._name:str = _name
        self._password_hash:str = None
        self._score:int = 0

    def __lt__(self, other) -> bool:
        return self.score < other.score

    def __eq__(self, other) -> bool:
        return self.score == other.score

    @property
    def uid(self) -> str:
        return self._uid
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def score(self) -> int:
        return self._score
    
    @score.setter
    def score(self, score:int):
        self._score += score
    
    def add_password(self, word:str) -> None:
        password = PasswordHasher()
        self._password_hash = password.hash(word)
    
    def verify_password(self, word:str) -> bool:
        password = PasswordHasher()
        try:
            return password.verify(self._password_hash, word)
        except argon2.exceptions.VerifyMismatchError:
            return False
        except AttributeError:
            return False

    @staticmethod
    def make_list(self, player_list:Player_List):
        players = []
        if player_list.head is not None:
            node = self._head
            while node is not None:
                players.append(node.player)
                node = node.next

        return players
    
    @staticmethod
    def player_sort(self, player_list:list):
        """Makes a sorted list from a linked list using score

        Args:
            Linked list to make the list
        """
        

            
        
    def __str__(self) -> str:
        return f"Player( name = {self._name} uid = {self._uid})"
    
    
