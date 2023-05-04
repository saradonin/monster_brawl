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

    def set_hp(self, damage_taken):
        self.hp = self.hp - damage_taken
        if self.hp > 0:
            return self.hp
        else:
            return f"{self.name} died!"


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

# create monsters
bug = Enemy('Bug', 1, 1, 4, 1, "It appears that this game is full of bugs!")
rat = Enemy('Rat', 1, 4, 2, 1, "Squeak!")
goblin = Enemy('Goblin', 2, 8, 1, 4, "I don't have time for this...")
orc = Enemy('Orc', 3, 16, 1, 8, "Victory or death! Aaaaarghh!")
owlbear = Enemy('Owlbear', 3, 20, 1, 6, "HOOT-GROWL!")
stone_golem = Enemy('Stone Golem', 4, 32, 1, 3, "Flesh. Weak. Return to the earth.")
froghemoth = Enemy('Froghemoth', 4, 60, 2, 4, "Aaaaaughibbrgubugbugrguburgle!")
elder_god = Enemy('The Elder God', 5, 1023, 1, 255, "All places, all things have souls. All souls can be devoured.")
monsters_list = [bug, rat, goblin, orc, owlbear, stone_golem, froghemoth, elder_god]

# test
# print(Creature.damage(elder_god, stone_golem))
# print(Creature.set_hp(orc, 2))

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
    :return: tuple (str, int, int, int) - class stats
    """
    choose_your_class = """Choose your class: 
      1. Warrior
      2. Rogue
      3. Mage
      4. Warlock
      """
    player_choice = validate_input(choose_your_class, len(player_char))
    player = player_char[int(player_choice - 1)]

    # return player.name, player.max_hp, player.hp, player.attacks_num, player.max_damage
    return player


def choose_enemy(win_counter=0):
    """
    Generates random monster form the list based on win counter, returns monster stats.
    :param win_counter: int - number of battles won
    :return: tuple (string, string, int, int, int) - monster stats
    """
    monster = monsters_list[random.randint(0, len(monsters_list) - 1)]
    # return monster.name, monster.intro, monster.max_hp, monster.hp, monster.attacks_num, monster.max_damage
    return monster

# test
# for i in range(0,10):
#     print(i, choose_enemy())



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
        else:
            enemy = choose_enemy(win_counter)
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

# print(validate_input(message, 4))
# print(choose_player_class())

print(fight())
