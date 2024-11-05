from app.player import Player
from app.player_bnode import PlayerBNode

class PlayerBST:
    
    def __init__(self) -> None:
        self._root = None
        self.players = []


    @property
    def root(self):
        return self._root
    

    def balance_tree(self):
        """Balances the binary tree. 
        It makes a ordered list.
        resets the _root to none
        and then inserts the nodes so that the tree is balanced.
        """
        self.in_order(self._root)
        self._root = None
        self.put_nodes_into_place(self.players)

    def middle(self, players):
        """Finds the middle index of a list.

        Args:
            players (list): list of player

        Returns:
            integer: index of the middle player
        """
        length = len(players)
        if length % 2 != 0:
            return length // 2
        return length // 2 -1


    def put_nodes_into_place(self, players):
        """Finds which node in the list should be a 
        root node to have a balanced tree.
        
        Checks if the list is zero, all the nodes have been put into binary tree.
        Checks if the list has two element and inserts them into binary tree.

        Finds middle node of the list and inserts that node into the binary tree.
        Then makes lists for either side of the middle and recursively dose the previously step.

        Args:
            players (list): list of player
        """
        if (len(players) == 0):
            return
        if (len(players) == 2):
            self.insert(players[0])
            self.insert(players[1])
            return
        middle = self.middle(players)
        node = players[middle]
        self.insert(node)
        
        self.put_nodes_into_place(players[:middle])
        self.put_nodes_into_place(players[middle+1:])
        
    
    def in_order(self, root):
        """Makes a ordered list from a binary tree.

        Args:
            root (node): The starting node of the binary tree.
        """
        if root is None:
            return
        self.in_order(root.left)
        self.players.append(root.player)
        self.in_order(root.right)


    def search(self, search_player:str):
        """Searches the binary tree for a node with a key that matches the search string.
        It dose this by recursively calling binary_search, if returns nothing search returns not found.
        
        Args:
            search_player (str):To search for

        Returns:
            string| Player object: if empty or no match returns string. else Player object.
        """
        if self.is_empty():            
            return "Binary Tree Empty."        
        tree_node = self._root
        
        search_result = PlayerBST.binary_search(search_player, tree_node)
        if search_result is None:
            return "No match found."
        else:
            return search_result.player

    
    def binary_search(search_player, tree_node):
        """Searches the binary tree for a node with a key that matches the search string.

        Args:
            search_player (string): name to find
            tree_node (node): To check and if not direct

        Returns:
            Player: object if found.
        """
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
        """Inserts a Player object into the right place in a binary tree.
        It dose this by calling binary_insert

        Args:
            player (Player): object
        """
        node = PlayerBNode(player)
        if self.is_empty():
            self._root = node
            return
        tree_node = self._root
        root = self._root        
        PlayerBST.binary_insert(node, tree_node, root)
        

    @staticmethod
    def binary_insert(node, tree_node, root):
        """Put the node into tree_node when finds the right place

        Args:
            node (Player): The player to insert
            tree_node (Player in binary tree): Starts at the root of the tree and traverses until gets to an empty leaf.
            root (last tree_node): Set the previous node, not ended up needed.
        """
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
    
    def display_players(self):
        for player in self.players:
            print(player)

    def display_tree(self, root):
        if root is None:
            return
        print(root.player)
        self.display_tree(root.left)
        self.display_tree(root.right)