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
    
    @tail.setter
    def tail(self, tail):
        self._tail = tail

    def is_empty(self) -> bool:
        return self._head is None
    
    def insert_first(self, player: Player):
        """_summary_

        Args:
            player (Player): _description_
        """
        new_node = Player_Node(player)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.pervious = new_node
            self._head = new_node

    def insert_last(self, player:Player):
        """_summary_

        Args:
            player (Player): _description_
        """
        new_node = Player_Node(player)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self.tail.next = new_node
            new_node.pervious = self._tail
            self._tail = new_node

    def delete_head(self):
        if self._head == self._tail:
            self._head = None
        else:
            node = self._head
            self._head = node.next
            del node

    def delete_tail(self):
        pass

    def delete_key(self, uid:str="", headTail:str="head"):
        """_summary_

        Args:
            uid (str): _description_
        """
        if self._head == self.tail:
            self._head = None
            self._tail = None
            
        if headTail == "head":
            node = self._head
            while node is not None:
                if node.key == uid:
                    pervious = node.pervious
                    next = node.next
                    if pervious is not None:
                        pervious.next = next
                    if next is not None:
                        next.pervious = pervious
                    del node
                    break
                node = node.next
                





                    



    
