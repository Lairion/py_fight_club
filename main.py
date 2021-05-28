# Random
from random import choice
from random import randint
from os.path import exists
# Character import
from characters import Character

# Armor imports
from armors import Armor, ModificationOfArmor, TypeOfArmor

# Weapon imports
from weapons import Weapon, TypeOfWeapon, ModificationOfWeapon

# json
import json

def create_choice_list(lst):
    print(*[f"[{i}] -- {str(lst[i]).capitalize()}" for i in range(len(lst))], sep='\n')


def mod(name, points, model):
    if model == 'arm_mod':
        return ModificationOfArmor(name, points)
    elif model == 'wpn_mod':
        return ModificationOfWeapon(name, points)
    elif model == 'arm_armor':
        return TypeOfArmor(name, points[0], points[1])
    elif model == 'wpn_weapon':
        return TypeOfWeapon(name, points[0], points[1])


def create_player():
    # Inputs
    # Input number of armor type
    create_choice_list(arm_types)
    arm_type_input = int(input("\nInput number of armor type: "))
    arm_name_input = input("Input name of your armor: ")
    character.suite_armor(Armor(arm_name_input, arm_types[arm_type_input]))

    # Input number of weapon type
    create_choice_list(wpn_types)
    wpn_type_input = int(input("\nInput number of weapon type: "))
    wpn_name_input = input("Input name of your weapon: ")
    hand_coeff_input = int(input("Input hand coefficient: "))
    character.take_weapon(Weapon(wpn_name_input, wpn_types[wpn_type_input], hand_coeff_input))

    # Input number of armor mod
    create_choice_list(arm_mods)
    arm_mod_input = int(input("\nInput number of armor mod: "))
    character.armor.add_modification(arm_mods[arm_mod_input])

    # Input number of weapon mod
    create_choice_list(wpn_mods)
    wpn_mod_input = int(input("\nInput number of armor mod: "))
    character.weapon.add_modification(wpn_mods[wpn_mod_input])

    data = {
        'armor_type': arm_type_input,
        'armor_mod': arm_mod_input,
        'armor_name': arm_name_input,
        'weapon_type': wpn_type_input,
        'weapon_mod': wpn_mod_input,
        'weapon_name': wpn_name_input,
        'hand_coeff': hand_coeff_input
    }

    with open('save.json', 'w') as outfile:
        json.dump(data, outfile)


parts_of_body = list(Character.damage_dict.keys())

arm_mods = [
    mod('Furniture of shadow', 2, 'arm_mod'),
    mod('Armadillo', 3, 'arm_mod'),
    mod('Resistance', 2, 'arm_mod'),
    mod('Fortune', 3, 'arm_mod'),
    mod('Aggression', 2, 'arm_mod'),
    mod('Fire resistance', 2, 'arm_mod'),
    mod('Antidote', 1, 'arm_mod'),
    mod('Impenetrability', 2, 'arm_mod')
]
wpn_mods = [
    mod('Fire', 7, 'wpn_mod'),
    mod('Poison', 8, 'wpn_mod'),
    mod("Magic pollination", 12, 'wpn_mod'),
    mod("Enchanted", 8, 'wpn_mod'),
    mod("Everything killer", 15, 'wpn_mod'),
    mod("Uncle Stepan's knife", 5, 'wpn_mod'),
    mod("God with you", 21, 'wpn_mod'),
    mod("Small superstrong help", 19, 'wpn_mod')
]
arm_types = [
    mod('fabric', [0, 'На такую нельзя надеется...'], 'arm_armor'),
    mod('leather', [1, 'В ней жарко и неудобно'], 'arm_armor'),
    mod('tin', [2, 'Такая себе, но на первое время хватит'], 'arm_armor'),
    mod('copper', [2, 'Защищает плохо, но красивая'], 'arm_armor'),
    mod('gold', [3, 'В глаза отсвечивает!'], 'arm_armor'),
    mod('lead', [3, 'Броня как броня'], 'arm_armor'),
    mod('iron', [4, 'В ней жарко, но хотя бы защищает'], 'arm_armor')
]
wpn_types = [
    mod('Sword', [30, 'Тяжелый но мощный'], 'wpn_weapon'),
    mod('Katana', [20, 'Легкая но хрупкая'], 'wpn_weapon')
]
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

enemies = [
    Character(choice(enemy_names)),
    Character(choice(enemy_names))
]
character = Character("You")

if exists('save.json'):
    load = input('Do you want to load a saved player? (y/n): ')

    if load == 'y':
        with open('save.json') as json_file:
            data = json.load(json_file)

            # Application
            character.suite_armor(Armor(data['armor_name'], arm_types[data['armor_type']]))
            character.take_weapon(Weapon(data['weapon_name'], wpn_types[data['weapon_type']], data['hand_coeff']))
            character.armor.add_modification(arm_mods[data['armor_mod']])
            character.weapon.add_modification(wpn_mods[data['weapon_mod']])
    else:
        create_player()
else:
    create_player()

for enemy in enemies:
    enemy.suite_armor(Armor(choice(arm_names), choice(arm_types)))
    enemy.take_weapon(Weapon(choice(wpn_names), choice(wpn_types), randint(1, 10)))
    enemy.weapon.add_modification(choice(wpn_mods))
    enemy.armor.add_modification(choice(arm_mods))

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
