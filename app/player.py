from argon2 import PasswordHasher
import argon2
import argon2.exceptions

class Player:
    """Holds the detail of the player
    """
    def __init__(self, _uid:str, _name:str) -> None:
        self._uid:str = _uid
        self._name:str = _name
        self._password_hash:str = None

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
        try:
            return password.verify(self._password_hash, word)
        except argon2.exceptions.VerifyMismatchError:
            return False
        except AttributeError:
            return False

    def __str__(self) -> str:
        return f"Player( name = {self._name} uid = {self._uid})"
        # return f"Player( name = {self._name} uid = {self._uid} password hash = {self._password_hash})"
    
    
