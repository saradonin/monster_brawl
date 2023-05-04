import random


class Creature:
    def __init__(self, name, max_hp, attacks_num, max_damage):
        self.name = name
        self.max_hp = max_hp
        self.attacks_num = attacks_num
        self.max_damage = max_damage
        self.hp = max_hp

    def damage(self, enemy):
        damage_done = 0
        for i in range(self.attacks_num):
            strike = random.randint(1, self.max_damage)
            print(f"{self.name} hit {enemy.name} for {strike} points of damage")
            damage_done += strike
        return damage_done


class PlayerClass(Creature):
    def __init__(self, name, max_hp, attacks_num, max_damage):
        super().__init__(name, max_hp, attacks_num, max_damage)




class Enemy(Creature):
    def __init__(self, name, level, max_hp, attacks_num, max_damage, intro):
        super().__init__(name, max_hp, attacks_num, max_damage)
        self.level = level
        self.intro = intro


# create player classes
warrior = PlayerClass('Warrior', 16, 1, 10)
rogue = PlayerClass('Rogue', 10, 3, 4)
mage = PlayerClass('Mage', 8, 1, 20)
warlock = PlayerClass('Warlock', 14, 4, 2)
player_char = [warrior, rogue, mage, warlock]

choose_your_class = """Choose your class: 
  1. Warrior
  2. Rogue
  3. Mage
  4. Warlock
  """

# create monsters
bug = Enemy('Bug', 1, 1, 4, 1, "It appears that this game is full of bugs!")
rat = Enemy('Rat', 1, 4, 2, 1, "Squeak!")
goblin = Enemy('Goblin', 2, 8, 1, 4, "I don't have time for this...")
orc = Enemy('Orc', 3, 16, 1, 8, "Victory or death! Aaaaarghh!")
owlbear = Enemy('Owlbear', 3, 20, 1, 6, "HOOT-GROWL!")
stone_golem = Enemy('Stone Golem', 4, 32, 1, 3, "Flesh. Weak. Return to the earth.")
froghemoth = Enemy('Froghemoth', 4, 60, 2, 4, "Aaaaaughibbrgubugbugrguburgle!")
elder_god = Enemy('The Elder God', 5, 1023, 1, 255, "All places, all things have souls. All souls can be devoured.")


print(Creature.damage(rogue, owlbear))
print(Creature.damage(owlbear, warrior))


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
    Takes user input and returns stats of player class.
    :return: tuple (int, int, int, int) - class stats
    """
    message = choose_your_class
    player_choice = validate_input(message, len(player_char))
    player_object = player_char[int(player_choice - 1)]

    player_name = player_object.name
    player_max_damage = player_object.max_damage
    player_attacks = player_object.attacks_num
    player_hp = player_object.max_hp
    return player_name, player_max_damage, player_attacks, player_hp

print(choose_player_class())

def choose_monster(win_counter):
    """
    Generates random monster form the list based on win counter, returns monster stats.
    :param win_counter: int - number of battles won
    :return: tuple (string, string, int, int, int) - monster stats
    """

    monster_index = len(monsters["name"]) - 1  # dict range
    if win_counter > 4:
        monster_type = random.randint(0, monster_index)
    elif win_counter > 2:
        monster_type = random.randint(0, monster_index - 2)  # without 2 of the strongest
    elif win_counter > 0:
        monster_type = random.randint(0, monster_index - 4)  # without 4 of the strongest
    else:
        monster_type = random.randint(0, monster_index - 5)  # without 5 of the strongest

    monster_name = monsters["name"][monster_type]
    monster_intro = monsters["intro"][monster_type]
    print(f"You encountered {monster_name}: {monster_intro}")
    monster_attacks = monsters["attacks"][monster_type]
    monster_max_damage = monsters["max_damage"][monster_type]
    monster_hp = monsters["hp"][monster_type]
    return monster_name, monster_intro, monster_attacks, monster_max_damage, monster_hp


def damage(name1, name2, max_damage, attacks):
    """
    Takes attacker stats and returns total amount of damage done by attacker.
    :param name1: str - attacker name
    :param name2: str - opponent name
    :param max_damage: int - max damage value
    :param attacks: int - number of attacks per turn
    :return: int - total damage done
    """
    damage_done = 0
    for i in range(attacks):
        strike = random.randint(1, max_damage)
        print(f"{name1} hit {name2} for {strike} points of damage")
        damage_done += strike
    return damage_done


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
    print("""Greetings adventurer! 
    Navigate through the game using buttons from [1] to [4] on your keyboard.
    """)
    player_index, player_max_damage, player_attacks, player_hp = choose_player_class()

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
        else:
            monster_name, monster_intro, monster_attacks, monster_max_damage, monster_hp = choose_monster(win_counter)

            while player_hp > 0 and monster_hp > 0:
                # monster attack turn
                monster_damage_done = damage(monster_name, "You", monster_max_damage, monster_attacks)
                player_hp -= monster_damage_done
                # player attack turn
                player_damage_done = damage("You", monster_name, player_max_damage, player_attacks)
                monster_hp -= player_damage_done

            else:  # win and loose conditions
                if player_hp > 0 >= monster_hp:
                    print("You won!")
                    win_counter += 1
                elif monster_hp > 0 <= player_hp:
                    print(f"You lost. {monster_name} won.")
                    return end_message(win_counter)
                else:
                    print("You both died.")
                    return end_message(win_counter)

# print(validate_input(message, 4))
# print(choose_player_class())

# print(fight())
