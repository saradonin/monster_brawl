import random
import data


def validate_input(message, num=2, player=None):
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

        if num == 2 and choice == "hero":
            player.level_up(2)
            print("Hero mode activated!")
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
    player_choice = validate_input(data.choose_your_class, len(data.player_char))
    player = data.player_char[int(player_choice - 1)]

    return player


def choose_enemy(player_level=1):
    """
    Returns random monster form the list based on player level.
    :param player_level: int
    :return: obj - enemy creature randomly generated object
    """
    while True:
        enemy = data.monsters_list[random.randint(0, len(data.monsters_list) - 1)]
        # ignores enemies way too easy or too hard
        if player_level - 2 <= enemy.level <= player_level + 1:
            print(f"You encountered {enemy.name} (level {enemy.level}): {enemy.intro}")
            enemy.hp = enemy.max_hp
            return enemy


def end_message(win_counter):
    """
    Prints ending message depending on how many matched player won
    :param win_counter: int - number of battles won
    :return: str - text message
    """
    if win_counter > 8:
        return f"You won {win_counter} battles today! Glorious!"
    elif win_counter >= 4:
        return f"You won {win_counter} battles today."
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
    FIGHT_OR_FLIGHT = """
Fight or flight? 
1. [FIGHT] I'd love to see a good brawl!
2. [FLIGHT] I'd rather stay home and read a book.
      """
    while True:
        decision = validate_input(FIGHT_OR_FLIGHT, 2, player)
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


# start the game
if __name__ == "__main__":
    fight()
