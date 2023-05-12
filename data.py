import gc
from creature import Creature
from enemy import Enemy


# DND damage types
ACID = 'Acid'
BLUDGEONING = 'Bludgeoning'
COLD = 'Cold'
FIRE = 'Fire'
FORCE = 'Force'
LIGHTNING = 'Lightning'
NECROTIC = 'Necrotic'
PIERCING = 'Piercing'
POISON = 'Poison'
PSYCHIC = 'Psychic'
RADIANT = 'Radiant'
SLASHING = 'Slashing'
THUNDER = 'Thunder'


# player data
# create player classes (name, level, max_hp, attacks_num, max_damage)
fighter = Creature('Fighter', 1, 16, 1, 10, (BLUDGEONING, SLASHING))
rogue = Creature('Rogue', 1, 12, 3, 4, (PIERCING, POISON))
sorcerer = Creature('Sorcerer', 1, 8, 1, 20, (COLD, FIRE, FORCE))
warlock = Creature('Warlock', 1, 14, 4, 2, (FORCE, NECROTIC, PSYCHIC))
choose_your_class = """Choose your class: 
  1. Fighter
  2. Rogue
  3. Sorcerer
  4. Warlock
  """
# create a list of player classes using gc module
player_char = [ob for ob in gc.get_objects() if isinstance(ob, Creature) and not isinstance(ob, Enemy)]

# enemy data
# create monsters Enemy('name, level, max_hp, attacks_num, max_damage, 'intro')
# level 0
bug = Enemy('Bug', 0, 2, 4, 1, (ACID, PIERCING), "It appears that this game is full of bugs!")
duckbunny = Enemy('Duckbunny', 0, 2, 1, 1, PIERCING,
                  "You see a rabbit with a duck's bill instead of a rabbit's snout. Why? WHY?!")
# level 1
kobold = Enemy('Kobold', 1, 5, 1, 4, (BLUDGEONING, PIERCING))
giant_rat = Enemy('Giant Rat', 1, 6, 2, 1, PIERCING, "Squeak!")
goblin = Enemy('Goblin', 1, 8, 1, 4, (PIERCING, SLASHING), "I don't have time for this...")
shrieker = Enemy('Shrieker', 1, 13, 1, 4, THUNDER)

# level 2
bandit = Enemy('Bandit', 2, 11, 1, 8, (PIERCING, SLASHING))
giant_centipede = Enemy('Giant Centipede', 2, 4, 2, 6, (PIERCING, POISON))
flying_sword = Enemy('Flying Sword', 2, 17, 1, 8, SLASHING)
poisonous_snake = Enemy('Poisonous Snake', 2, 12, 4, 2, (PIERCING, POISON), "Sssss...")
shadow = Enemy('Shadow', 2, 16, 1, 12, NECROTIC)
skeleton = Enemy('Skeleton', 2, 12, 1, 6, (BLUDGEONING, PIERCING))

# level 3
hobgoblin = Enemy('Hobgoblin', 3, 18, 1, 8, (PIERCING, SLASHING))
gray_ooze = Enemy('Gray Ooze', 3, 22, 1, 4, (ACID, BLUDGEONING))
mimic = Enemy('Mimic', 3, 58, 2, 4, (BLUDGEONING, LIGHTNING), "What’s in the box?")
orc = Enemy('Orc', 3, 16, 1, 16, (PIERCING, SLASHING), "Victory or death!")
violet_fungus = Enemy('Violet Fungus', 3, 18, 4, 3, NECROTIC)
zombie = Enemy('Zombie', 3, 22, 1, 6, BLUDGEONING)

# level 4
basilisk = Enemy('Basilisk', 4, 52, 1, 6, (PIERCING, POISON))
gelatinous_cube = Enemy('Gelatinous Cube', 4, 84, 1, 2, (ACID, FORCE), "Bloop!")
owlbear = Enemy('Owlbear', 4, 59, 1, 10, (PIERCING, SLASHING), "HOOT-GROWL!")
ogre = Enemy('Ogre', 4, 50, 1, 13, BLUDGEONING, "Stupid puny thing! Me smash!")
will_o_wisp = Enemy('Will-O’-Wisp', 4, 22, 2, 16, LIGHTNING)

# level 5
ghost = Enemy('Ghost', 5, 45, 1, 17, (FORCE, NECROTIC), "Whoo-oo-oo-oo...")
mummy = Enemy('Mummy', 5, 58, 1, 12, (BLUDGEONING, NECROTIC))
nightmare = Enemy('Nightmare', 5, 68, 2, 8, (BLUDGEONING, FIRE), "I have so much to show you...")


# level 6
ettin = Enemy('Ettin', 6, 85, 2, 16, (PIERCING, SLASHING))
troll = Enemy('Troll', 6, 84, 3, 7, (PIERCING, SLASHING))
chimera = Enemy('Chimera', 6, 114, 1, 12, (BLUDGEONING, PIERCING, SLASHING))

# level 7
black_dragon = Enemy('Black Dragon', 7, 127, 1, 15, (ACID, SLASHING))
froghemoth = Enemy('Froghemoth', 7, 80, 2, 12, (ACID, BLUDGEONING), "Aaaaaughibbrgubugbugrguburgle!")
roper = Enemy('Roper', 7, 93, 4, 24, PIERCING)

# level 8
hydra = Enemy('Hydra', 8, 172, 3, 10, (PIERCING, COLD))
beholder = Enemy('Beholder', 8, 180, 1, 36, (FORCE, NECROTIC),
                 "All places, all things have souls. All souls can be devoured.")
stone_giant = Enemy('Stone Giant', 8, 126, 1, 40, BLUDGEONING, "Flesh. Weak. Return to the earth.")

# level 9
angel = Enemy('Angel', 9, 243, 3, 24, (FIRE, PIERCING, RADIANT))
demon = Enemy('Demon', 9, 262, 4, 12, (FIRE, SLASHING), "Everything you love will burn!")
lich = Enemy('Lich', 9, 135, 2, 40, (ACID, COLD, FIRE, FORCE, THUNDER),
             "Very well... witness what I have seen and TREMBLE!")

# level 10
elder_god = Enemy('The Elder God', 10, 800, 1, 150, (FORCE, PSYCHIC), "Release your grip on hope!")
kraken = Enemy('Kraken', 10, 472, 3, 40, (PIERCING, LIGHTNING))
red_dragon = Enemy('The Great Red Dragon', 10, 546, 3, 26, (BLUDGEONING, FIRE, SLASHING),
                   "You and the others, you owe me awe.")

# create a list of monsters using gc module
monsters_list = [ob for ob in gc.get_objects() if isinstance(ob, Enemy)]
