import random
from dialogues import greetings, fight_or_flight, choose_your_class, bye_answer, player_char, monsters


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

    :return: tuple (int, int, int, int)
    """
    message = choose_your_class
    player_choice = validate_input(message, len(player_char["name"]))
    player_index = int(player_choice) - 1

    player_max_damage = player_char["max_damage"][player_index]
    player_attacks = player_char["attacks"][player_index]
    player_hp = player_char["hp"][player_index]
    return player_index, player_max_damage, player_attacks, player_hp


def choose_monster():
    """

    :return: tuple (string, string, int, int, int)
    """
    # picking a monster
    monster_index = len(monsters["name"]) - 1
    monster_type = random.randint(0, monster_index)
    monster_name = monsters["name"][monster_type]
    monster_intro = monsters["intro"][monster_type]
    print(f"You encountered {monster_name}: {monster_intro}")
    monster_attacks = monsters["attacks"][monster_type]
    monster_max_damage = monsters["max_damage"][monster_type]
    monster_hp = monsters["hp"][monster_type]
    return monster_name, monster_intro, monster_attacks, monster_max_damage, monster_hp


def end_message(win_counter):
    """Prints ending message depending on how many matched player won
    :param win_counter: int - number of battles won
    :return: str - text message
    """
    if win_counter > 4:
        print(f"You won {win_counter} battles today! Glorious! Songs of your victories will be sung in every inn.")
    elif win_counter >= 1:
        print(f"You won {win_counter} battles today. Not bad for a novice.")
    else:
        print(f"You won {win_counter} battles today. What a shame.")


def fight():
    print(greetings)
    player_index, player_max_damage, player_attacks, player_hp = choose_player_class()

    win_counter = 0

    while True:
        decision = validate_input(fight_or_flight, 2)
        if decision == 2:
            print(bye_answer)
            break
        else:
            monster_name, monster_intro, monster_attacks, monster_max_damage, monster_hp = choose_monster()

            while player_hp > 0 and monster_hp > 0:

                monster_damage_done = 0
                for i in range(monster_attacks):
                    monster_strike = random.randint(1, monster_max_damage)
                    print(f"{monster_name} hit you for {monster_strike} points of damage")
                    monster_damage_done += monster_strike
                player_hp -= monster_damage_done

                player_damage_done = 0
                for i in range(player_attacks):
                    player_strike = random.randint(1, player_max_damage)
                    print(f"You hit {monster_name} for {player_strike} points of damage")
                    player_damage_done += player_strike
                monster_hp -= player_damage_done

            else:  # win and loose conditions
                if monster_hp <= 0 and player_hp > 0:
                    print("You won!")
                    win_counter += 1
                elif player_hp <= 0 and monster_hp > 0:
                    print(f"You lost. {monster_name} won.")
                    end_message(win_counter)
                    break
                else:
                    print("You both died.")
                    end_message(win_counter)
                    break


message = "Wpisz coś"
# print(validate_input(message, 4))
# print(choose_player_class())

print(fight())
