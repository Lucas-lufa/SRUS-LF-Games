from app.player import Player
from app.player_node import Player_Node


class Player_List:
    """Manages the double link list.
    Contains Player_Node instances
    """

    def __init__(self) -> None:
        self._head:Player_Node = None
        self._tail:Player_Node = None

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
        """Checks to see if list is empty.

        Returns:
            bool: if the head has an object, truthy or is None, falsy.
        """
        return self._head is None
    
    def insert_first(self, player: Player):
        """Inserts a node at the head of the list.

        Args:
            player (Player): A Player instance is pass to the Player_Node on creation of one of it's instance.
            Then inserts the instance in the appropriate location.
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
        """Inserts a node at he tail of the list.

        Args:
            player (Player): player (Player): A Player instance is pass to the Player_Node on creation of one of it's instance.
            Then inserts the instance in the appropriate location.
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
        """Delete the head node.
        It will delete the list if there is only one node.
        """
        if self.is_empty():
            return
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            node = self._head
            self._head = node.next
            del node

    def delete_tail(self):
        """Deletes the tail node.
        It will delete the list if there is only one node.
        """
        if self.is_empty():
            return
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            node = self._tail
            self._tail = self.tail.pervious
            del node

    def delete_key(self, uid:str="", headTail:str="head"):
        """Deletes node via the key.

        Args:
            uid (str, optional): key for the node. Defaults to "".
            headTail (str, optional): Sets the direction to search from. Defaults to "head".
            TODO Implement tail direction.
        """
        if self._head == self.tail:
            self._head = None
            self._tail = None
            return
            
        if headTail == "head":
            node = self._head
            while node is not None:
                if node.key == uid:                    
                    if node == self._head:
                        self.delete_head()
                        break
                    if node == self._tail:
                        self.delete_tail()
                        break
                    pervious = node.pervious
                    next = node.next
                    if pervious is not None:
                        pervious.next = next
                    if next is not None:
                        next.pervious = pervious
                    del node
                    break
                node = node.next

    def display(self, forward:bool = True):
        """Prints each node in the list

        Args:
            forward (bool, optional): Control direction of printing, True head to tail. Defaults to True.
        """
        if self.is_empty():
            print("Player list is empty.")
        if forward:
            node = self._head
            while node is not None:
                print(f"{node}")
                node = node.next
        else:
            node = self._tail
            while node is not None:
                print(f"{node}")
                node = node.pervious




                    



    
