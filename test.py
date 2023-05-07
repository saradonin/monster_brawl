import main
import creature as cr
import enemy as en

# change value to 1 or True to run a test
TEST_LEVEL_UP_FIGHTER = 1
TEST_LEVEL_UP_ROGUE = 1
TEST_LEVEL_UP_SORCERER = 1
TEST_LEVEL_UP_WARLOCK = 1
TEST_CHOOSE_ENEMY = 0


def test_level_up(creature, max_level):
    result = f"{creature.name}: level {creature.level}, hp {creature.max_hp}, dmg {creature.max_damage}, " \
             f"stat {creature.max_hp + creature.attacks_num * creature.max_damage} \n"
    for i in range(-1, max_level):
        creature.level_up()
        result += f"{creature.name}: level {creature.level}, hp {creature.max_hp}, dmg {creature.max_damage}, " \
                  f"stat {creature.max_hp + creature.attacks_num * creature.max_damage} \n"
    return result


def test_choose_enemy(level, number):
    result = f"Enemies for player level {level} \n"
    for i in range(number):
        enemy = main.choose_enemy(level)
        result += f"{enemy.name}: level {enemy.level} \n"
    return result


if TEST_LEVEL_UP_FIGHTER:
    print(test_level_up(cr.fighter, 9))
if TEST_LEVEL_UP_ROGUE:
    print(test_level_up(cr.rogue, 9))
if TEST_LEVEL_UP_SORCERER:
    print(test_level_up(cr.sorcerer, 9))
if TEST_LEVEL_UP_WARLOCK:
    print(test_level_up(cr.warlock, 9))

if TEST_CHOOSE_ENEMY:
    print(test_choose_enemy(3, 10))
