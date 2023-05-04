import random


class Creature:
    """
    A base class that represents a creature in a game.

    :ivar name: str - The name of the creature.
    :ivar max_hp: int - The maximum hit points of the creature.
    :ivar attacks_num: int - The number of attacks the creature can make.
    :ivar max_damage: int - The maximum amount of damage the creature can deal.
    :ivar hp: int - The current hit points of the creature, initialized to max_hp.

    :param name: str - The name of the creature.
    :param max_hp: int - The maximum hit points of the creature.
    :param attacks_num: int - The number of attacks the creature can make.
    :param max_damage: int - The maximum amount of damage the creature can deal.
    """

    def __init__(self, name, max_hp, attacks_num, max_damage):
        self.name = name
        self.max_hp = max_hp
        self.attacks_num = attacks_num
        self.max_damage = max_damage

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
            print(f"{self.name} hit {enemy.name} for {strike} points of damage")
            damage_done += strike
        return damage_done


class Enemy(Creature):
    """
    A class that represents an enemy creature in a game. Inherits from the Creature base class.

    :ivar level: int - The level of the enemy creature.
    :ivar intro: str - A string describing the enemy creature.

    :param name: str - The name of the enemy creature.
    :param level: int - The level of the enemy creature.
    :param max_hp: int - The maximum hit points of the enemy creature.
    :param attacks_num: int - The number of attacks the enemy creature can make.
    :param max_damage: int - The maximum amount of damage the enemy creature can deal.
    :param intro: str - A string describing the enemy creature.
    """

    def __init__(self, name, level, max_hp, attacks_num, max_damage, intro):
        super().__init__(name, max_hp, attacks_num, max_damage)
        self.level = level
        self.intro = intro


# create player classes (name, max_hp, attacks_num, max_damage)
warrior = Creature('Warrior', 16, 1, 10)
rogue = Creature('Rogue', 10, 3, 4)
mage = Creature('Mage', 8, 1, 20)
warlock = Creature('Warlock', 14, 4, 2)
choose_your_class = """Choose your class: 
  1. Warrior
  2. Rogue
  3. Mage
  4. Warlock
  """
player_char = [warrior, rogue, mage, warlock]

# create monsters (name, level, max_hp, attacks_num, max_damage, intro)
bug = Enemy('Bug', 0, 1, 4, 1, "It appears that this game is full of bugs!")
rat = Enemy('Rat', 0, 4, 2, 1, "Squeak!")
goblin = Enemy('Goblin', 1, 8, 1, 4, "I don't have time for this...")
orc = Enemy('Orc', 2, 16, 1, 8, "Victory or death! Aaaaarghh!")
owlbear = Enemy('Owlbear', 3, 20, 1, 6, "HOOT-GROWL!")
stone_golem = Enemy('Stone Golem', 4, 32, 1, 3, "Flesh. Weak. Return to the earth.")
froghemoth = Enemy('Froghemoth', 4, 60, 2, 4, "Aaaaaughibbrgubugbugrguburgle!")
elder_god = Enemy('The Elder God', 5, 1023, 1, 255, "All places, all things have souls. All souls can be devoured.")
monsters_list = [bug, rat, goblin, orc, owlbear, stone_golem, froghemoth, elder_god]


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


def choose_enemy(win_counter=0):
    """
    Generates random monster form the list based on win counter, returns monster stats.
    :param win_counter: int - number of battles won
    :return: obj - enemy creature randomly generated object
    """
    while True:
        monster = monsters_list[random.randint(0, len(monsters_list) - 1)]
        if monster.level <= win_counter:  # only chooses monsters with level lower on equal win counter
            return monster
        else:
            continue


def end_message(win_counter):
    """
    Prints ending message depending on how many matched player won
    :param win_counter: int - number of battles won
    :return: str - text message
    """
    if win_counter > 4:
        return f"You won {win_counter} battles today! Glorious! Songs of your victories will be sung in every inn."
    elif win_counter >= 1:
        return f"You won {win_counter} battles today. Not bad for a novice."
    else:
        return f"You won {win_counter} battles today. What a shame."


def fight():
    """
    This is where the fight happens.
    :return: str - end message
    """
    print("Greetings adventurer! \nNavigate through the game using buttons from [1] to [4] on your keyboard.\n")
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
            enemy = choose_enemy(win_counter)
            enemy.hp = enemy.max_hp
            player.hp = player.max_hp

            while player.hp > 0 and enemy.hp > 0:
                # monster attack turn
                monster_damage_done = enemy.damage(player)
                player.hp -= monster_damage_done
                # player attack turn
                player_damage_done = player.damage(enemy)
                enemy.hp -= player_damage_done

            else:  # win and loose conditions
                if player.hp > 0 >= enemy.hp:
                    print("You won!")
                    win_counter += 1
                elif enemy.hp > 0 <= player.hp:
                    print(f"You lost. {enemy.name} won.")
                    return end_message(win_counter)
                else:
                    print("You both died.")
                    return end_message(win_counter)


print(fight())
