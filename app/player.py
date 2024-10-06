from argon2 import PasswordHasher
import argon2
import argon2.exceptions

#from app.player_list import Player_List

class Player:
    """Holds the detail of the player
    """
    def __init__(self, _uid:str, _name:str) -> None:
        self._uid:str = _uid
        self._name:str = _name
        self._password_hash:str = None
        self._score:int = 0

    def __lt__(self, other) -> bool:
        return self._score < other.score

    def __eq__(self, other) -> bool:
        return self._score == other.score
    
    def __gt__(self, other) -> bool:
        return self._score > other.score

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
    def make_list(player_list):
        players = []
        if player_list.head is not None:
            node = player_list._head
            while node is not None:
                players.append(node.player)
                node = node.next

        return players
    
    @staticmethod
    def partition(players, i, j):
        """_summary_
        https://youtu.be/7h1s2SojIRw?si=CkL1_j2xALGK_wQC&t=723

        Args:
            players (_type_): _description_
            i (_type_): _description_
            j (_type_): _description_

        Returns:
            _type_: _description_
        """

        pivot = i
        
        while i < j:
            # low = players[i] 
            # high = players[j] 
            # pivotValue = players[pivot]
            
            # i pointer is looking for smaller than pivot. if doesn't find will increment pointer
            while True:
                i+=1
                if players[pivot] > players[i]:
                    break

            # j pointer looks for larger than pivot, if doesn't find will increment pointer
            while True:
                j-=1
                if players[pivot] < players[j] or players[pivot] == players[j]:
                    if i < j:                    
                     (players[i], players[j]) = (players[j], players[i])
                    break
            
        (players[j], players[pivot]) = (players[pivot], players[j])

        return j
    
    @staticmethod
    def quick_sort(players, low, high):
        if (len(players[low:high]) <= 1):
            return

        pivot = Player.partition(players, low, high)
        
        Player.quick_sort(players, low, pivot)
        Player.quick_sort(players, pivot + 1, high)
            
    @staticmethod
    def player_sort(players:list):
        """Makes a sorted list from a linked list using score

        Args:
            Linked list to make the list
        """

        # players = Player.make_list() //for now make sure other works than this.

        Player.quick_sort(players, 0, len(players)-1)
        

        


            


                
        



            
        
    def __str__(self) -> str:
        return f"Player( name = {self._name} uid = {self._uid})"
    
    
