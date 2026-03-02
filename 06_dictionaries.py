# 06_dictionaries.py
# dictionaries and attack mechanics

import random

player = {
    "name": input("Enter your name: "),
    "hp" :100,
    "atk":25,
    "def":10,

}

print("\nPlayer Created")
print(player)

enemy_attack = random.randint(player["atk"]-5, player["atk"]+5)

print("\nEnemy attacked with:",enemy_attack)

damage = enemy_attack - player["def"]

if damage < 0:
    damage = 0

player["hp"] -= damage

if player["hp"] < 0:
    player["hp"] = 0

print("Damage Taken: ",damage)
print("Remaining Hp:",player["hp"])

