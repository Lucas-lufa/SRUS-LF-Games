from app.player import Player


class Player_Node:
    """_summary_
    """
    def __init__(self) -> None:
        self._player = None
        self._next = None
        self._pervious = None

    @property
    def player(self):
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

    #creating a new property variable called key

    @property
    def key(self):
        return self._player.uid
    
    def __str__(self) -> str:
        return f"{self._player} next= {self._next} pervious= {self._pervious}"
    
