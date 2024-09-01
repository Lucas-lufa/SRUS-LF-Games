from app.player_list import Player_List
from app.player import Player

player_list = Player_List()
player = Player("1", "Luke")
player.add_password('12')
player_list.insert_first(player)
print(f"Head {player_list.head}")
print(f"Tail {player_list.tail}")

player = Player("2","John" )
player.add_password('12')
player_list.insert_first(player)
print(f"Head {player_list.head}")
print(f"Tail {player_list.tail}")

player = Player("3","Fad")
print(player.verify_password('12'))
player.add_password('12')
print(player.verify_password('12'))
print(player.verify_password('1'))
player_list.insert_first(player)
print(f"Head {player_list.head}")
print(f"Tail {player_list.tail}")

player_list.display(False)
player_list.delete_key('2')
print()
player_list.display(False)

print()