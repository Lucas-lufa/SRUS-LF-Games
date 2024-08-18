from app.player import Player


class Player_Node:
    """Contains a player instance.
    Controls the next and previous for the link list.
    """
    def __init__(self, player:Player) -> None:
        self._player = player
        self._next = None
        self._pervious = None

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
        return f"{self._player}"

    def __repr__(self) -> str:
        return f"{self._player} next= {self._next!r} pervious= {self._pervious!r}"
    
