# Random
from random import choice
# Character import
from characters import Character

# Armor imports
from armors import Armor, ModificationOfArmor, TypeOfArmor

# Weapon imports
from weapons import Weapon, TypeOfWeapon, ModificationOfWeapon

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
weapon_mods = [ModificationOfWeapon(k, v) for k, v in modifications_of_weapon.items()]
weapon_types = [TypeOfWeapon(k, *v) for k, v in types_of_weapon.items()]

characters = [
    Character("You"),
    Character("Enemy")
]

characters[0].suite_armor(Armor("Megasuite", armor_types[-1]))
characters[1].suite_armor(Armor("Megaleather", armor_types[1]))
characters[0].take_weapon(Weapon("Takagero", weapon_types[1], 2))
characters[1].take_weapon(Weapon("Excalibre", weapon_types[0], 3))
characters[0].weapon.add_modification(weapon_mods[1])
characters[1].weapon.add_modification(weapon_mods[0])
dict_of_part = {str(i): part_of_body[i] for i in range(len(part_of_body))}
option_descr = [f"{k}-{v}" for k, v in dict_of_part.items()]

# <<<<<<< HEAD

# Add cicle(while). That cicle should finish if somebody dead.
# Show who win!

while not characters[0].hp <= 0 or not characters[1].hp <= 0:
    characters[0].hit(
        dict_of_part
        [input("\nHIT. Input one of next options:\n" + "\n".join(option_descr).replace('-', ' -- ') +
               '\n\nYour choice: ')])

    characters[0].defence(
        dict_of_part
        [input("\nDEFENCE. Input one of next options:\n" + "\n".join(option_descr).replace('-', ' -- ') +
               '\n\nYour choice: ')])

    # choices
    characters[1].hit(choice(part_of_body))
    characters[1].defence(choice(part_of_body))
    characters[0] - characters[1]
    characters[1] - characters[0]

    # stats
    for entity in characters:
        print(f'\nStats of {entity.name}:\n\nHP = "{entity.hp}",\nArmor = "{entity.armor.name}",\nHited part of body: "'
              f'{entity.hited}",\nDefenced part of body: "{entity.defenced}"')

    # check for a winner
    if characters[0].hp == 0:
        winner = 1
        break
    elif characters[1].hp == 0:
        winner = 0
        break

print(f'\nThe winner is... {characters[winner].name}!!!')


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
