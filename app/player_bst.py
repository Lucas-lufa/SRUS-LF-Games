from app.player import Player
from app.player_bnode import PlayerBNode

class PlayerBST:
    
    def __init__(self) -> None:
        self._root = None

    @property
    def root(self):
        return self._root
    
    def insert(self, player:Player):

        node = PlayerBNode(player)
        tree_node = self._root
        root = self._root
        
        if self.is_empty():
            self._root = node
            return
        
        PlayerBST.binary_insert(node, tree_node, root)

    @staticmethod
    def binary_insert(node, tree_node, root):
        if (node.player.name == tree_node.player.name):
            tree_node.player = node.player
        else:
            if (node.player.name < tree_node.player.name):
                if tree_node.left is None:
                    tree_node.left = node
                    tree_node.left.root = root
                else:
                    root = tree_node
                    tree_node = tree_node.left
                    PlayerBST.binary_insert(node, tree_node, root)
            else:
                if tree_node.right is None:
                    tree_node.right = node
                    tree_node.right.root = root
                else:
                    root = tree_node
                    tree_node = tree_node.right
                    PlayerBST.binary_insert(node, tree_node, root)
        

    def is_empty(self) -> bool:
        """Checks to see if binary search tree is empty.

        Returns:
            bool: if the root has an object, truthy or is None, falsy.
        """
        return self._root is None