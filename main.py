# Random
from random import choice
# Character import
from characters import Character

# Armor imports
from armors import Armor, ModificationOfArmor, TypeOfArmor

# Weapon imports
from weapons import Weapon, TypeOfWeapon, ModificationOfWeapon

def option_descr(lst):
    return [f"{i} - {lst[i]}" for i in range(len(lst))]

part_of_body = list(Character.damage_dict.keys())
modifications_of_armor = {
    'chestplate': 150,
    'leggings': 100,
    'helmet': 90,
    'boots': 80,
    'furniture of shadow': 200,
    'armadillo': 100,
    'resist!': 20,
    'fortune': 15,
    'aggression': 30,
    'Unfire': 300,
    'antidote': 250,
    'impenetrability': 300,
}
modifications_of_weapon = {
    'fire': 15,
    'poison': 10,
    "Magic pollination": 17,
    "Mesmerized by Vasya": 5,
    "Silver knife, which can kill everything": 23,
    "Knife from uncle Stepan": 7,
    "God with you": 48,
    "Little help with your superstrong": 45,
}
types_of_armor = {
    'fabric': [0, 'На такую нельзя надеется...'],
    'leather': [1, 'В ней жарко и неудобно'],
    'tin': [2, 'Такая себе, но на первое время хватит'],
    'copper': [2, 'Защищает плохо, но красивая'],
    'gold': [3, 'В глаза отсвечивает!'],
    'lead': [3, 'Броня как броня'],
    'iron': [4, 'В ней жарко, но хотябы защищает']
}
types_of_weapon = {
    'sword': [30, 'Тяжелый но мощный'],
    'katana': [20, 'Легкая но хрупкая'],
}


def mod(name, points, type):
    if type == 'armor':
        return ModificationOfArmor(name, points)
    elif type == 'weapon':
        return ModificationOfWeapon(name, points)


armor_mods = [ModificationOfArmor(k, v) for k, v in modifications_of_armor.items()]

armor_modifications = []
cnt = -1
for name, protect in modifications_of_armor.items():
    cnt += 1
    armor_modifications.append(mod(name, protect, "armor"))

armor_types = [TypeOfArmor(k, *v) for k, v in types_of_armor.items()]
# armor_mods = [ModificationOfArmor(k, v) for k, v in armor_modifications.items()]
weapon_mods = [ModificationOfWeapon(k, v) for k, v in modifications_of_weapon.items()]
weapon_types = [TypeOfWeapon(k, *v) for k, v in types_of_weapon.items()]

enemies = [
    Character("Enemy1"),
    Character("Enemy2")
]

character = Character("You")
#####

print(*option_descr(armor_types), sep="\n")
arm_type = int(input("Input armor type:"))
character.suite_armor(Armor(input("Input name of your armor:"), armor_types[arm_type]))
print(*option_descr(weapon_types), sep="\n")
wpn_type = int(input("Input weapon type:"))
character.take_weapon(Weapon(input("Input name of your weapon:"), weapon_types[wpn_type], int(input("Input coeficient:"))))


print(*option_descr(weapon_mods), sep="\n")
mods_wpn = int(input("Input weapon modification:"))
character.weapon.add_modification(weapon_mods[mods_wpn])
print(character.weapon)
print(character.armor)

# print(*option_descr(armor_modifications), sep="\n")
# mods_arm = int(input("Input armor modification:"))
# character.armor.add_modification(armor_mods[mods_arm])
# print(character.armor)

# 1. Add modifications use same princip like previous code.
# 2. Use random count of modifications






# ctrl+?
# Override this part of code using cicle and random
# while character.hp>0:
#     enemies[0].suite_armor(Armor(choice(types_of_armor)))
#     enemies[0].take_weapon(Weapon(choice(types_of_weapon), choice(modifications_of_weapon)))
#     enemies[1].suite_armor(Armor(choice(types_of_armor)))
#     enemies[1].take_weapon(Weapon(choice(types_of_weapon), choice(modifications_of_weapon)))
#     print(enemies[1].weapon, enemies[1].armor)
#     print(enemies[0].weapon, enemies[0].armor)
######



# adapt this code for fighting character and enemies[0]
# dict_of_part = {str(i):part_of_body[i] for i in range(len(part_of_body))}
# option_descr = [f"{k}-{v}" for k, v in dict_of_part.items()]
# while character.hp > 0 and enemies[0].hp > 0:
#     character.hit(
#         dict_of_part[
#             input("HIT.Input one of next options:\n"+"\n".join(option_descr)+"\nInput:")
#         ]
#     )
#     character - enemies[0]#[input("HIT.Input one of enemies:\n"+"\n".join(enemies)+"\nInput:")]
#     enemies[0] - character
#     for entity in character:
#         print(entity)
# else:
#     winner = character > enemies[0]
#     if winner:
#         print("Winner:", winner.name )
#         print("Loser:", (character < enemies[0]).name)
#     else:
#         print("No winner")
######

    # if characters[0].hp > characters[1].hp:
    #     winner = 0
    # elif characters[0].hp == characters[1].hp:
    #     winner = None
    # else:
    #     winner = 1
    # if winner is not None:
    #     print(f'\nThe winner is... {characters[winner].name}!!!')


    # stats


    # check for a winner
    # if characters[0].hp == 0:
    #     winner = 1
    #     break
    # elif characters[1].hp == 0:
    #     winner = 0
    #     break




# Help
# print(characters[0] - characters[1])
# print(characters[1] - characters[0])
#
# TypeOfArmor("gold",3,"В глаза отсвечивает!")
# TypeOfWeapon("gold",3,"В глаза отсвечивает!")
#
# ModificationOfArmor("Furniture of shadow",1)
# ModificationOfWeapon("Stone of shadow", 200)
# hero_weapon = Weapon("Sword of Freeze", 400, 2)
# hero_armor = Armor("Shealder", "gold")
# hero_armor2 = Armor("Shealder2", "lead")
# hero = Character("Peter")
# hero.armor.hint()
# hero.suite_armor(hero_armor2)
# hero.armor.hint()
# print(hero.weapon.name)

# >>>>>>> bceb0463d186604a8b5c63337283d33717a7d7e2
