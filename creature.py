import random
import math


class Creature:
    """
    A base class that represents a creature in a game.

    :ivar name: str - The name of the creature.
    :ivar max_hp: int - The maximum hit points of the creature.
    :ivar attacks_num: int - The number of attacks the creature can make.
    :ivar max_damage: int - The maximum amount of damage the creature can deal.
    :ivar level: int - The level of the creature.

    :param name: str - The name of the creature.
    :param max_hp: int - The maximum hit points of the creature.
    :param attacks_num: int - The number of attacks the creature can make.
    :param max_damage: int - The maximum amount of damage the creature can deal.
    """

    def __init__(self, name, level, max_hp, attacks_num, max_damage, damage_type=()):
        self.name = name
        self.max_hp = max_hp
        self.attacks_num = attacks_num
        self.max_damage = max_damage
        self.level = level
        self.damage_type = damage_type

    def damage(self, enemy):
        """
        Calculates the amount of damage the creature can deal to an enemy.

        :param enemy: obj - the enemy that the creature is attacking
        :return: int - total amount of damage dealt to the enemy
        """
        from enemy import Enemy  # import inside function to avoid circular import error
        damage_done = 0
        for i in range(self.attacks_num):
            strike = random.randint(1, self.max_damage)
            if isinstance(self.damage_type, tuple):
                damage_type = self.damage_type[random.randint(0, len(self.damage_type) - 1)]
            else:
                damage_type = self.damage_type
            if not isinstance(self, Enemy):
                print(f"You hit {enemy.name} for {strike} points of {damage_type} damage")
            else:
                print(f"{self.name} hit you for {strike} points of {damage_type} damage")
            damage_done += strike
        return damage_done

    def level_up(self):
        modifier = 1.2
        self.level += 1
        self.max_hp = math.ceil(self.max_hp * modifier + self.level * 2)
        self.max_damage = math.ceil(self.max_damage * modifier)
        return f"You reached level {self.level}!"
