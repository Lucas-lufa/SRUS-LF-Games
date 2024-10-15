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
        if score > 0:
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
        """Makes a list form list from the linked list.

        Args:
            player_list (Player_List): Double linked list.

        Returns:
            list: List of player objects.
        """
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
        
        Places the pivot into the correct place in the list, 
        returns it's index so sub lists can be made.

        Args:
            players (list): list to be mutated and sorted. 
            i (integer): Pointer moving from the start to the end.
            j (integer): Pointer moving from the end to the start.

        Returns:
            integer: Pivot point moved into it's place in the list.
        """

        pivot = i
        
        while i < j:            
        # i pointer is looking for smaller than pivot. if doesn't find will increment pointer
            while True:
                i+=1
                if players[pivot] > players[i]:
                    break
        # j pointer looks for larger than pivot, if doesn't find will increment pointer
            while True:
                j-=1
        # If both pointers stop and the j pointer has not crossed the i pointer 
                if players[pivot] < players[j] or players[pivot] == players[j]:
                    if i < j:
        # Swap object at i pointer with object at j pointer
                     (players[i], players[j]) = (players[j], players[i])
                    break
        # If pointer j crosses i pointer swap object at j pointer with object at pivot pointer.
        (players[j], players[pivot]) = (players[pivot], players[j])
        # index that will be used for lower and upper value of sub list.
        return j
    
    @staticmethod
    def quick_sort(players, low, high):
        """
        https://youtu.be/7h1s2SojIRw?si=CkL1_j2xALGK_wQC&t=723
        
        Sorts a list in descending order by using a quicksort algorithm.

        Args:
            players (list): list to be mutated and sorted.
            low (int): The lower bound of list or sub list to find pivot position.
            high (int): The upper bound of list or sub list to find pivot position.
        """
        if (len(players[low:high]) <= 1):
            return

        pivot = Player.partition(players, low, high)
        
        Player.quick_sort(players, low, pivot)
        Player.quick_sort(players, pivot + 1, high)
        
    def __str__(self) -> str:
        return f"Player( name = {self._name} uid = {self._uid})"
    
    
