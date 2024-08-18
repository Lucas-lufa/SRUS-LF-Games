class Player:
    """Holds the detail of the player
    """
    def __init__(self, _uid:str, _name:str) -> None:
        self._uid = _uid
        self._name = _name

    @property
    def uid(self) -> str:
        return self._uid
    
    @property
    def name(self) -> str:
        return self._name
    
    def __str__(self) -> str:
        return f"Player( name = {self._name} uid = {self._uid} )"
    
