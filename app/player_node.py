from app.player import Player


class Player_Node:
    """Contains a player instance.
    Controls the next and previous for the link list.
    """
    def __init__(self, player:Player) -> None:
        self._player:Player = player
        self._next:Player_Node = None
        self._pervious:Player_Node = None

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        return self._player

    @property
    def next(self):
        return self._next
    
    @property
    def next_print(self):
        if self._next is None:
            return "None"
        return self._next._player.__str__()
    
    @property
    def pervious_print(self):
        if self._pervious is None:
            return "None"
        return self._pervious._player.__str__()
    
    @property
    def pervious(self):
        return self._pervious
    
    @next.setter
    def next(self, next):
        self._next = next

    @pervious.setter
    def pervious(self, pervious):
        self._pervious = pervious


    @property
    def key(self):
        return self._player.uid
    
    def __str__(self) -> str:
        return f"{self._player} next= {self.next_print} pervious= {self.pervious_print}"
    
