from app.player import Player
from app.player_bnode import PlayerBNode

class PlayerBST:
    
    def __init__(self) -> None:
        self._root = None

    @property
    def root(self):
        return self._root
    
    def search(self, search_player:str):

        if self.is_empty():            
            return "Binary Tree Empty."        
        tree_node = self._root
        
        search_result = PlayerBST.binary_search(search_player, tree_node)
        if search_result is None:
            return "No match found."
        else:
            return search_result.player


        
    def binary_search(search_player, tree_node):

        if (tree_node is None):
            return tree_node
        if (search_player == tree_node.player.name):
            return tree_node
        if (search_player < tree_node.player.name):
            tree_node = tree_node.left
            PlayerBST.binary_search(search_player, tree_node)
        else:
            tree_node = tree_node.right
            PlayerBST.binary_search(search_player, tree_node)

        return PlayerBST.binary_search(search_player, tree_node)

    def insert(self, player:Player):

        node = PlayerBNode(player)
        if self.is_empty():
            self._root = node
            return
        tree_node = self._root
        root = self._root        
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