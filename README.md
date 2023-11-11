
# Monster Brawl #

***

This is a simple creature battle game that allows the player to choose their character class and fight against various monsters. 
The player can choose from four different character classes, each with their own unique stats.

## Prerequisites ##
Python 3.x should be installed on your machine.

## How to play ##
1. Clone the repository to your local machine.
2. Run the main.py file 
3. Follow the on-screen instructions to play the game.
4. Choose your character class by typing the corresponding number (1-4).
5. Battle monsters.
6. If you win the fight, you will be matched against a stronger monster in the next fight.

## How to run Monster Brawl Dockerized ##

1. Build & Run:
```
docker build . -t monster-app
docker run -it --name monster-brawl monster-app
```
2. Follow steps 3-6 from *How to play* section
3. Stop Container:
```
docker stop monster-brawl
```
4. Restart the container:
```
docker start monster-brawl && exec -it monster-brawl python3 main.py
```
Ensure you have [Docker](https://www.docker.com/get-started/) installed before running these commands.

## Classes ## 
There are four classes that the player can choose from:

1. Warrior - high health, high damage
2. Rogue - low health, high damage, multiple attacks
3. Mage - low health, very high damage, single attack
4. Warlock - medium health, low damage, multiple attack


![brawl](https://github.com/saradonin/monster_brawl/assets/124811561/5bc449b2-025b-4357-85c8-adc46964d425)
