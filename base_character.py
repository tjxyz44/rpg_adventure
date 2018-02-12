class BaseCharacter:
    def __init__(self, name, level, health, armor):
        self.name = name
        self.level = level
        self.armor = armor
        self.health = health


    def enemies(self, resistance):
        self.resistance = resistance

    def player(self, gear):
        pass


# virt = BaseCharacter(1, 5, 7)
#
# skeleton.enemies(2)
# zombie.enemies(0)
#
# print(skeleton.resistance)
