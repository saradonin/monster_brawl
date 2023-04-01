import random
from dialogues import greetings, fight_or_flight, choose_your_class, player_char, monsters


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
    player_choice = validate_input(message, len(player_char["name"]))
    player_index = int(player_choice) - 1

    player_max_damage = player_char["max_damage"][player_index]
    player_attacks = player_char["attacks"][player_index]
    player_hp = player_char["hp"][player_index]
    return player_index, player_max_damage, player_attacks, player_hp


def choose_monster(win_counter):
    """
    Generates random monster form the list, returns monster stats.
    :return: tuple (string, string, int, int, int)
    """
    monster_index = len(monsters["name"]) - 1  # dict range
    if win_counter > 4:
        monster_type = random.randint(0, monster_index)
    elif win_counter > 2:
        monster_type = random.randint(0, monster_index - 1)  # without strongest
    elif win_counter > 0:
        monster_type = random.randint(0, monster_index - 2)  # without 2 of the strongest
    else:
        monster_type = random.randint(0, monster_index - 3)  # without 3 of the strongest

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
    print(greetings)
    player_index, player_max_damage, player_attacks, player_hp = choose_player_class()

    win_counter = 0

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

print(fight())
