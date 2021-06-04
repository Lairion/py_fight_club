# json
import json
# Random
from random import choice, randint
from os.path import exists
# Character import
from characters import Character
# Armor imports
from armors import Armor, ModificationOfArmor, TypeOfArmor
# Weapon imports
from weapons import Weapon, TypeOfWeapon, ModificationOfWeapon

def create_choice_list(lst):
    print(*[f"[{i}] -- {str(lst[i]).capitalize()}" for i in range(len(lst))], sep='\n')


def create_player(data, arm_types, wpn_types, arm_mods, wpn_mods):
    # Inputs
    # Input number of armor type
    character = Character(data["character"])
    character.suite_armor(Armor(data['armor_name'], arm_types[data['armor_type']]))
    character.take_weapon(Weapon(data['weapon_name'], wpn_types[data['weapon_type']], data['hand_coeff']))
    character.armor.add_modification(arm_mods[data['armor_mod']])
    character.weapon.add_modification(wpn_mods[data['weapon_mod']])
    with open(f'characters/save/{data["character"]}.json', 'w') as outfile:
        json.dump(data, outfile)
    return character


parts_of_body = list(Character.damage_dict.keys())

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
arm_names = [
    'Leather',
    'Sunshine armor',
    'Shadow night',
    'Desert sea',
    'Demon slayer'
]
wpn_names = [
    'Sword',
    'Katana'
]
enemy_names = [
    'Rick Astley',
    'Rick',
    'Tom',
    'George',
    'Morty',
    'John',
    'Sans',
    'Jack',
    'Theodore',
    'Gabriel',
    'Leo',
    'Lincoln',
    'Christopher',
    'Andrew',
    'Thomas',
    'Rayan',
    'Jeremiah',
    'Ezekiel',
    'Roman',
    'Easton',
    'Miles',
    'Robert ',
    'Jameson ',
    'Nicholas',
    'Greyson'
]
armor_types = [TypeOfArmor(k, *v) for k, v in types_of_armor.items()]
armor_mods = [
    ModificationOfArmor(k, v) for k, v in  json.load(
        open('armors/armor_mods/list_of_modification.json')).items()
]
weapon_mods = [
    ModificationOfWeapon(k, v) for k, v in json.load(
        open('weapons/weapon_mods/list_of_modification.json')).items()
]
weapon_types = [TypeOfWeapon(k, *v) for k, v in types_of_weapon.items()]
enemies = [
    Character(choice(enemy_names)),
    Character(choice(enemy_names))
]
load = input('Do you want to load a saved player? (y/n): ')
if load == 'y':
    if exists('save.json'):
        with open('save.json') as json_file:
            data = json.load(json_file)
            # Application
            create_player(data, armor_types, weapon_types, armor_mods, weapon_mods)
else:
    data = {}
    data.update({'character' : input("Input player name: ")})
    data.update({'armor_type': int(input("Input number of armor type: ")),
    'armor_name': input("Input name of your armor: "),
    'armor_mod': int(input("Input number of armor mod: ")),
    'weapon_type': int(input("Input number of weapon type: ")),
    'weapon_name': input("Input name of your weapon: "),
    'hand_coeff': int(input("Input hand coefficient: ")),
    'weapon_mod': int(input("Input number of weapon mod: "))})
    character = create_player(data, armor_types, weapon_types, armor_mods, weapon_mods)

for enemy in enemies:
    enemy.suite_armor(Armor(choice(arm_names), choice(armor_types)))
    enemy.take_weapon(Weapon(choice(wpn_names), choice(weapon_types), randint(1, 10)))
    enemy.weapon.add_modification(choice(weapon_mods))
    enemy.armor.add_modification(choice(armor_mods))

while character.hp > 0 and (enemies[0].hp + enemies[1].hp) > 0:

    # Player's hit part input
    create_choice_list(parts_of_body)
    character.hit(parts_of_body[int(input("\nHIT. Input number of options: "))])

    # Player's defence part input
    create_choice_list(parts_of_body)
    character.defence(parts_of_body[int(input("\nDEF. Input number of options: "))])

    # enemy attacks player and player attacks enemy
    for enemy in enemies:
        enemy.hit(choice(parts_of_body))
        enemy.defence(choice(parts_of_body))
        character - enemy
        enemy - character

    # stats
    print('\n')
    print(enemies[0])
    print(enemies[1])
    print(character)
    print('\n')

else:
    winner = character > enemies[0]
    if winner is None:
        print("Winner is... Nobody.")
    else:
        winner = winner > enemies[1]
        if winner is None:
            print("Winner is... Nobody.")
        else:
            if winner.name == character.name:
                print("Winner is... You!")
                print(f"Losers are {enemies[0].name}, {enemies[1].name}")
            else:
                print(f"Winner are... {enemies[0].name}, {enemies[1].name}!")
                print(f"Loser is You")
