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

playera = Player("1","a")
playerb = Player("2","b" )
playerc = Player("3","c")
playerd = Player("4","d")
playere = Player("5","e")
playerf = Player("6","f")

bst = PlayerBST()

bst.insert(playerf)
bst.insert(playerc)
bst.insert(playerb)
bst.insert(playere)
bst.insert(playera)
bst.insert(playerd)

# bst.in_order(bst.root)
# bst.put_nodes_into_place(bst.players)
print("Pre-order")
bst.display_tree(bst.root)
bst.balance_tree()
print("")
print("Balanced tree")
bst.display_tree(bst.root)
print(bst.players)
