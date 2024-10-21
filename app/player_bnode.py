class PlayerBNode:

    def __init__(self, player) -> None:
        self._player = player
        self._root = None
        self._left = None
        self._right = None

    @property
    def player(self):
        return self._player
    
    @property
    def root(self):
        return self._root

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right
    
    @player.setter
    def player(self, player):
        self._player = player

    @root.setter
    def root(self, root):
        self._root = root
    
    @left.setter
    def left(self, node):
        self._left = node

    @right.setter
    def right(self, node):
        self._right = node