from rpg_adventure.enemy import Enemy
from rpg_adventure.player import Player
from rpg_adventure.weapon import Weapon
from rpg_adventure.chest import Chest


skeleton = Enemy('skeleton', 1, 5, 1, 1, 0, 7)

bronze_sword = Weapon('bronze sword', 1, 6, "fire")

print('Fonsi: Hello, Welcome to the world of italianus, My name is Fonsi, I will be your guide through this journey.')
print("Please tell me your name:"'\n')

player1 = input('Enter your name. 5 character limit. ')

while True:
        if len(player1) <= 5:
                print("cool name {}!"'\n'.format(player1))
                break
        player1 = input("Invalid, Try Again. Enter your name. 5 character limit.")

player1 = Player(player1, 1, 10, 0)

rock = Weapon('rock', 1, 2, 3)
paper = Weapon('paper', 1, 2, 3)
scissor = Weapon('scissor', 1, 2, 3)

chest1 = Chest([rock, paper, scissor])
chest1.chest_contents()







# print(player1.__dict__)
#
# print(player1.experience)
#
# print(skeleton.health)
# print(player1.health)
#
# skeleton.attack(player1)
#
# print(player1.__dict__)
