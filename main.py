from app.player_list import Player_List
from app.player import Player

player_list = Player_List()
player = Player("1", "Luke")
player_list.insert_first(player)
print(f"Head {player_list.head}")
print(f"Tail {player_list.tail}")

player = Player("2","John")
player_list.insert_last(player)
print(f"Head {player_list.head}")
print(f"Tail {player_list.tail}")

player = Player("3","Fad")
player_list.insert_first(player)
print(f"Head {player_list.head}")
print(f"Tail {player_list.tail}")
print()