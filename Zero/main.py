# Character import
from characters import Character

# Armor imports
from armors import Armor, ModificationOfArmor, TypeOfArmor

# Weapon imports
from weapons import Weapon, TypeOfWeapon, ModificationOfWeapon

# Import random
from random import randint

types_of_armor = [
    ['fabric', 0, 'На такую нельзя надеется...'],
    ['leather', 1, 'В ней жарко и неудобно'],
    ['tin', 2, 'Такая себе, но на первое время хватит'],
    ['copper', 2, 'Защищает плохо, но красивая'],
    ['gold', 3, 'В глаза отсвечивает!'],
    ['lead', 3, 'Броня как броня'],
    ['iron', 4, 'В ней жарко, но хотябы защищает'],
    ['none', 0, 'None armor']
]
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
    'fire': 150,
    'poison': 100,
}
types_of_weapon = [
    ['sword', 30, 'Тяжелый но мощный'],
    ['katana', 20, 'Легкая но хрупкая']
]

# armor_mods = [ModificationOfArmor(k, v) for k, v in modifications_of_armor.items()]
# armor_types = [TypeOfArmor(k, *v) for k, v in Character.types_of_armor.items()]
# weapon_mods = [ModificationOfWeapon(k, v) for k, v in modifications_of_weapon.items()]
# weapon_types = [TypeOfWeapon(k, *v) for k, v in types_of_weapon.items()]

characters = [
    Character("You", TypeOfWeapon('hand', 1, 'None weapon')),
    Character("Enemy", TypeOfWeapon('hand', 1, 'None weapon'))
]

characters[0].take_weapon(Weapon('hand', 1, 'None weapon'))
characters[1].take_weapon(Weapon('hand', 1, 'None weapon'))
characters[0].suite_armor(TypeOfArmor(types_of_armor[-1][0], types_of_armor[-1][1], types_of_armor[-1][2]))
characters[1].suite_armor(TypeOfArmor(types_of_armor[-1][0], types_of_armor[-1][1], types_of_armor[-1][2]))

parts_of_body = []
for part in characters[0].bonus_damage_dict.keys():
    parts_of_body.append(part)

while not characters[0].hp <= 0 or not characters[1].hp <= 0:
    characters[0].hit(input('Action: Hit. Select the part of body (head, hand, body, leg): '))
    characters[0].defence(input('Action: Defence. Select the part of body (head, hand, body, leg): '))
    characters[1].hit(parts_of_body[randint(0, 3)])
    characters[1].defence(parts_of_body[randint(0, 3)])
    print(f'You attacked the enemy part of body: {characters[0].attacked_part_of_body}')
    print(f'Enemy defenced the his part of body: {characters[1].defenced_part_of_body}')
    print('\n-=-=-=-=-\n' + (characters[0] - characters[1]))
    if not characters[0].hp <= 0 or not characters[1].hp <= 0:
        break
    print(f'Enemy attacked the your part of body: {characters[1].attacked_part_of_body}')
    print(f'You defenced the your part of body: {characters[0].defenced_part_of_body}')
    print('\n-=-=-=-=-\n' + (characters[1] - characters[0]))

if characters[0].hp > characters[1].hp:
    print('You win!')
else:
    print('You lose...')
