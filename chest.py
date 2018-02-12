import random

from rpg_adventure.weapon import Weapon


class Chest:

    def __init__(self, item_list):
        self.item_list = item_list

    def open_chest(self):
        return random.choice(self.item_list)

    def chest_contents(self):
        for some_item in self.item_list:
            print(some_item.__dict__)

#
# sword = Weapon('sword', 1, 3, 'water')
# bow = Weapon('bow', 1, 4, 'water')
# staff = Weapon('staff', 1, 5, 'water')
#
# chest = Chest([sword, bow, staff])
#
# item = chest.open_chest()
# print(item.__dict__)

# weapons = \
#     {
#         'sword': Weapon('sword', 1, 3, 'water'),
#         'bow': Weapon('bow', 1, 4, 'water')
#     }
#
# sword = weapons['sword']
