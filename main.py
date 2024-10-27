from app.player_list import Player_List
from app.player import Player
from app.player_bst import PlayerBST
from app.player_bnode import PlayerBNode

# player_list = Player_List()
# player = Player("1", "Luke")
# player.add_password('12')
# player_list.insert_first(player)
# print(f"Head {player_list.head}")
# print(f"Tail {player_list.tail}")

# player = Player("2","John" )
# player.add_password('12')
# player_list.insert_first(player)
# print(f"Head {player_list.head}")
# print(f"Tail {player_list.tail}")

# player = Player("3","Fad")
# print(player.verify_password('12'))
# player.add_password('12')
# print(player.verify_password('12'))
# print(player.verify_password('1'))
# player_list.insert_first(player)
# print(f"Head {player_list.head}")
# print(f"Tail {player_list.tail}")

# player_list.display(False)
# player_list.delete_key('2')
# print()
# player_list.display(False)

player0 = Player("1", "Luke")
player1 = Player("2","John" )
player2 = Player("3","Fad")
player3 = Player("4","Kule")
player4 = Player("5","Ohnj")
player5 = Player("6","Daf")

bst = PlayerBST()

print(bst.search('Ohnj'))
bst.insert(player0)
bst.insert(player4)
bst.insert(player1)
print(bst.search('Fad'))
bst.insert(player2)
bst.insert(player3)
bst.insert(player5)
print(bst.search('Daf'))



print(bst)
