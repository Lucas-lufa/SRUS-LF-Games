from argon2 import PasswordHasher

class Player:
    """Holds the detail of the player
    """
    def __init__(self, _uid:str, _name:str) -> None:
        self._uid = _uid
        self._name = _name
        self._password_hash = None

    @property
    def uid(self) -> str:
        return self._uid
    
    @property
    def name(self) -> str:
        return self._name
    
    def add_password(self, word:str) -> None:
        password = PasswordHasher()
        self._password_hash = password.hash(word)
    
    def verify_password(self, word:str) -> bool:
        password = PasswordHasher()
        return password.verify(self._password_hash, word)

    def __str__(self) -> str:
        #return f"Player( name = {self._name} uid = {self._uid})"
        return f"Player( name = {self._name} uid = {self._uid} password hash = {self._password_hash})"
    
    
