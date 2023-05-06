import random
import math
import gc


class Creature:
    """
    A base class that represents a creature in a game.

    :ivar name: str - The name of the creature.
    :ivar max_hp: int - The maximum hit points of the creature.
    :ivar attacks_num: int - The number of attacks the creature can make.
    :ivar max_damage: int - The maximum amount of damage the creature can deal.
    :ivar hp: int - The current hit points of the creature, initialized to max_hp.
    :ivar level: int - The level of the creature.

    :param name: str - The name of the creature.
    :param max_hp: int - The maximum hit points of the creature.
    :param attacks_num: int - The number of attacks the creature can make.
    :param max_damage: int - The maximum amount of damage the creature can deal.
    """

    def __init__(self, name, max_hp, attacks_num, max_damage, level=1):
        self.name = name
        self.max_hp = max_hp
        self.attacks_num = attacks_num
        self.max_damage = max_damage
        self.level = level
        self.hp = max_hp

    def damage(self, enemy):
        """
        Calculates the amount of damage the creature can deal to an enemy.

        :param enemy: obj - the enemy that the creature is attacking
        :return: int - total amount of damage dealt to the enemy
        """
        damage_done = 0
        for i in range(self.attacks_num):
            strike = random.randint(1, self.max_damage)
            if self in player_char:
                print(f"You hit {enemy.name} for {strike} points of damage")
            elif enemy in player_char:
                print(f"{self.name} hit you for {strike} points of damage")
            damage_done += strike
        return damage_done

    def level_up(self):
        modifier = 1.2
        self.level += 1
        self.max_hp = math.ceil(self.max_hp * modifier + self.level * 2)
        self.max_damage = math.ceil(self.max_damage * modifier)
        return f"You reached level {self.level}!"


class Enemy(Creature):
    """
    A class that represents an enemy creature in a game. Inherits from the Creature base class.

    :ivar intro: str - A string describing the enemy creature.

    :param name: str - The name of the enemy creature.
    :param level: int - The level of the enemy creature.
    :param max_hp: int - The maximum hit points of the enemy creature.
    :param attacks_num: int - The number of attacks the enemy creature can make.
    :param max_damage: int - The maximum amount of damage the enemy creature can deal.
    :param intro: str - A string describing the enemy creature.
    """

    def __init__(self, name, level, max_hp, attacks_num, max_damage, intro):
        super().__init__(name, level, max_hp, attacks_num, max_damage)
        self.intro = intro


# create player classes (name, max_hp, attacks_num, max_damage)
fighter = Creature('Fighter', 16, 1, 10)
rogue = Creature('Rogue', 10, 3, 4)
sorcerer = Creature('Sorcerer', 8, 1, 20)
warlock = Creature('Warlock', 14, 4, 2)
choose_your_class = """Choose your class: 
  1. Fighter
  2. Rogue
  3. Sorcerer
  4. Warlock
  """
# create a list of player classes using gc module
player_char = [ob for ob in gc.get_objects() if isinstance(ob, Creature) and not isinstance(ob, Enemy)]

# create monsters Enemy(‘name’, max_hp, attacks_num, max_damage, level, ‘intro’)
# level 0
bug = Enemy('Bug', 1, 4, 1, 0, "It appears that this game is full of bugs!")
duckbunny = Enemy('Duckbunny', 2, 1, 1, 0,
                  "You see a rabbit with a duck's bill instead of a rabbit's snout. Why? WHY?!")
rat = Enemy('Rat', 4, 2, 1, 0, "Squeak!")
# level 1
goblin = Enemy('Goblin', 8, 1, 4, 1, "I don't have time for this...")
gelatinous_cube = Enemy('Gelatinous Cube', 16, 1, 2, 1, "Bloop!")
# level 2
mimic = Enemy('Mimic', 16, 2, 4, 2, "What’s in the box?")
orc = Enemy('Orc', 16, 1, 8, 2, "Victory or death! Aaaaarghh!")
# level 3
owlbear = Enemy('Owlbear', 20, 1, 6, 3, "HOOT-GROWL!")
# level 4
stone_golem = Enemy('Stone Golem', 32, 1, 3, 4, "Flesh. Weak. Return to the earth.")
froghemoth = Enemy('Froghemoth', 60, 2, 4, 4, "Aaaaaughibbrgubugbugrguburgle!")
# level 5
beholder = Enemy('Beholder', 40, 1, 40, 5, "All places, all things have souls. All souls can be devoured.")
# level 7
elder_god = Enemy('The Elder God', 1023, 1, 255, 7, "Release your grip on hope!")

# create a list of monsters using gc module
monsters_list = [ob for ob in gc.get_objects() if isinstance(ob, Enemy)]


def validate_input(message, num=2):
    """
    Prompts user to make a choice, validates input.
    :param message: string - prompt
    :param num: int - upper range of possible answers
    :return: int - player choice
    """
    while True:
        choice = input(message)

        # test for empty string
        if choice == "":
            print("Invalid input. Try again.")
            continue

        if choice in "123456789"[0:num] and len(choice) == 1:
            return int(choice)
        else:
            print("Invalid input. Try again.")


def choose_player_class():
    """
    Prompts the player to choose their character class from a list of options.
    :return: obj - player's chosen character class object
    """
    player_choice = validate_input(choose_your_class, len(player_char))
    player = player_char[int(player_choice - 1)]

    return player


def choose_enemy(player_level=1):
    """
    Returns random monster form the list based on player level.
    :param player_level: int
    :return: obj - enemy creature randomly generated object
    """
    while True:
        enemy = monsters_list[random.randint(0, len(monsters_list) - 1)]
        # ignores enemies way too easy or too hard
        if player_level - 2 <= enemy.level <= player_level + 1:
            print(f"You encountered {enemy.name} (level: {enemy.level}): {enemy.intro}")
            enemy.hp = enemy.max_hp
            return enemy


def end_message(win_counter):
    """
    Prints ending message depending on how many matched player won
    :param win_counter: int - number of battles won
    :return: str - text message
    """
    if win_counter > 8:
        return f"You won {win_counter} battles today! Glorious! Songs of your victories will be sung in every inn."
    elif win_counter >= 4:
        return f"You won {win_counter} battles today. Not bad for a novice."
    else:
        return f"You won {win_counter} battles today. What a shame."


def fight():
    """
    Simulates a fight between the player and enemies.
    :return: str - end message
    """
    print("Greetings adventurer!")
    print("Navigate through the game using buttons from [1] to [4] on your keyboard.\n")
    player = choose_player_class()

    win_counter = 0
    fight_or_flight = """
Fight or flight? 
1. [FIGHT] I'd love to see a good brawl!
2. [FLIGHT] I'd rather stay home and read a book.
      """
    while True:
        decision = validate_input(fight_or_flight, 2)
        if decision == 2:
            return "Ok then, bye! Come back later."
        elif decision == 1:
            enemy = choose_enemy(player.level)
            player.hp = player.max_hp

            # monster attack turn if alive
            while enemy.hp > 0:
                monster_damage_done = enemy.damage(player)
                player.hp -= monster_damage_done

                # player attack turn if alive
                if player.hp > 0:
                    player_damage_done = player.damage(enemy)
                    enemy.hp -= player_damage_done

                else:
                    print(f"You lost. {enemy.name} won.")
                    return end_message(win_counter)

            print("You won!")
            win_counter += 1
            # level up every 5 wins
            if not win_counter % 5:
                print(player.level_up())


def main():
    game_end = fight()
    print(game_end)


# start the game
if __name__ == "__main__":
    main()
