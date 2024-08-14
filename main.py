from app.player_list import Player_List
from app.player import Player

player_list = Player_List()
player = Player("1", "Luke")
player_list.insert_last(player)
player = Player("2","John")
print(player)
player_list.insert_last(player)
print(player_list.head)
print(player_list.tail)