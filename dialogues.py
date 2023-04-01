# This file only contains dialogues and dictionaries necessary for the game.


greetings = """Greetings adventurer! 
Navigate through the game using buttons from [1] to [4] on your keyboard.
"""

fight_or_flight = """
Fight or flight? 
  1. [FIGHT] I'd love to see a good brawl!
  2. [FLIGHT] I'd rather stay home and read a book.
  """

intro_bug = "It appears that this game is full of bugs!"
intro_rat = "Squeak!"
intro_goblin = "I don't have time for this..."
intro_orc = "Victory or death! Aaaaarghh!"
intro_owlbear = "HOOT-GROWL!"
intro_stone_golem = "Flesh. Weak. Return to the earth."
froghemoth_into = "Aaaaaughibbrgubugbugrguburgle!"
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
    "name": ["Bug", "Rat", "Goblin", "Orc",
             "Owlbear", "Stone Golem", "Froghemoth", "The Elder God"],
    "hp": [1, 4, 8, 16, 20, 32, 60, 1023],
    "max_damage": [1, 1, 4, 8, 6, 3, 4, 255],
    "attacks": [4, 2, 1, 1, 1, 1, 2, 1],
    "intro": [intro_bug, intro_rat, intro_goblin, intro_orc,
              intro_owlbear, intro_stone_golem, froghemoth_into, intro_the_elder_god]
}
