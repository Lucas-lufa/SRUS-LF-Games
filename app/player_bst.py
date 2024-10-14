from app.player import Player
from app.player_bnode import PlayerBNode

class PlayerBST:
    
    def __init__(self, root) -> None:
        self._root = root

    @property
    def _root(self):
        return self._root
    
    def insert(self, player:Player):

        node = PlayerBNode(player)
        root = self._root

        if self.is_empty():
            self._root = node
            return
        
        PlayerBST.binary_insert(node, root)

    @staticmethod
    def binary_insert(self, node, root):
        if (ord(node.player.name) < ord(root.player.name)):
            if root.left is None:
                root.left = node
            else:
                root = root.left
                PlayerBST.binary_insert(node, root)
        else:
            if root.right is None:
                root.right = node
            else:
                root = root.right
                PlayerBST.binary_insert(node, root)
        

    def is_empty(self) -> bool:
        """Checks to see if binary search tree is empty.

        Returns:
            bool: if the root has an object, truthy or is None, falsy.
        """
        return self._root is None