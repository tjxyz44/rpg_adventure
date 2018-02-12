from rpg_adventure.base_character import BaseCharacter


class Player (BaseCharacter):

    weapon = None
    experience = 0

    def __init__(self, name, level, health, armor):
        super().__init__(name, level, health, armor)

    def wield_weapon(self, weapon):
        self.weapon = weapon

    def attack(self, enemy):
        enemy.health -= (self.weapon.damage - enemy.armor)
        print(f"You attack the enemy. He has: {enemy.health} health remaining")

        if enemy.check_death():
            self.add_experience(enemy.experience)

    def add_experience(self, experience):
        self.experience += experience




