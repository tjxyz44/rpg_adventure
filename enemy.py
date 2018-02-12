from rpg_adventure.base_character import BaseCharacter


class Enemy(BaseCharacter):
    def __init__(self, name, level, health, armor, damage, resistance, experience):
        super().__init__(name, level, health, armor)
        self.damage = damage
        self.resistance = resistance
        self.experience = experience

    def death(self):
        pass

    def check_death(self):
        if self.health > 0:
            return False

        return True

    def attack(self, player):
        player.health -= self.damage
        print(f"{self.name} bit your ass. You have: {player.health} hp remaining")



