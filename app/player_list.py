from app.player import Player
from app.player_node import Player_Node


class Player_List:
    """_summary_
    """

    def __init__(self) -> None:
        self._head = None
        self._tail = None

    @property
    def head(self):
        return self._head
    
    @head.setter
    def head(self, head):
        self._head = head

    @property
    def tail(self):
        return self._tail
    
    @head.setter
    def tail(self, tail):
        self._tail = tail

    def is_empty(self) -> bool:
        return self._head is None
    
    def insert_first(self, player: Player):
        """
        docstring
        """
        new_node = Player_Node(player)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
            return

        new_node.next = self._head
        self._head.pervious = new_node
        self.head = new_node