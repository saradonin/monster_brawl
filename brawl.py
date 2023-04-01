import random


# dialogues
greetings = """Greetings adventurer! 
Navigate through the game using buttons from [1] to [4] on your keyboard.
"""

fight_or_flight = """Fight or flight? 
  1. [FIGHT] I'd love to see a good brawl!
  2. [FLIGHT] I'd rather stay home and read a book.
  """
bye_answer = "Ok then, bye! Come back later."
wrong_answer = "I knew you'd try it. Let's settle this in a civilized manner. Try again. \n"
intro_bug = "It appears that this game is full of bugs!"
intro_rat = "Squeak!"
intro_goblin = "I don't have time for this..."
intro_orc = "Victory or death! Aaaaarghh!"
intro_stone_golem = "Flesh. Weak. Return to the earth."
intro_the_elder_god = "All places, all things have souls. All souls can be devoured."

choose_your_class = """Choose your class: 
  1. Fighter
  2. Rogue
  3. Sorcerer
  4. Warlock
  """
player_char = {
    "name": ["Fighter", "Rogue", "Sorcerer", "Warlock"],
    "hp": [16, 10, 8, 14],
    "max_damage": [10, 4, 20, 2],
    "attacks": [1, 3, 1, 4],
}
monsters = {
    "name": ["Bug", "Rat", "Goblin",
             "Orc", "Stone Golem", "The Elder God"],
    "hp": [1, 4, 8, 16, 32, 1023],
    "max_damage": [1, 1, 4, 8, 3, 255],
    "attacks": [4, 2, 1, 1, 1, 1],
    "intro": [intro_bug, intro_rat, intro_goblin,
              intro_orc, intro_stone_golem, intro_the_elder_god]
}



def validate_input(message, num=2):
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
    message = choose_your_class
    player_choice = validate_input(message, len(player_char["name"]))
    player_index = int(player_choice) - 1

    player_max_damage = player_char["max_damage"][player_index]
    player_attacks = player_char["attacks"][player_index]
    player_hp = player_char["hp"][player_index]
    return player_index, player_max_damage, player_attacks, player_hp

def choose_monster():
    # picking a monster
    monster_index = len(monsters["name"]) - 1
    monster_type = random.randint(0, monster_index)
    monster_name = monsters["name"][monster_type]
    monster_intro = monsters["intro"][monster_type]
    monster_attacks = monsters["attacks"][monster_type]
    monster_max_damage = monsters["max_damage"][monster_type]
    monster_hp = monsters["hp"][monster_type]
    return monster_name, monster_intro, monster_attacks, monster_max_damage, monster_hp

def end_message(win_counter):
    """Prints ending message depending on how many matched player won
    :param win_counter: int
    :return: Text message
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
                    print("You won!", "\n")
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