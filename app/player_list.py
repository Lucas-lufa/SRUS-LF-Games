from app.player import Player
from app.player_node import PlayerNode


class Player_List:
    """_summary_
    """

    def __init__(self) -> None:
        self._head = None

    @property
    def head(self):
        return self._head
    
    @head.setter
    def head(self, head):
        self._head = head

    def is_empty(self) -> bool:
        return self._head is None
    
    def insert_first(self, player: Player):
        """
        docstring
        """
        new_node = PlayerNode(player)

        if self.is_empty():
            self.head = new_node