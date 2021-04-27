# Character import
from characters import Character

# Armor imports
from armors import Armor, ModificationOfArmor, TypeOfArmor

# Weapon imports
from weapons import Weapon, TypeOfWeapon, ModificationOfWeapon

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
types_of_armor = {
    'fabric': [0,'На такую нельзя надеется...'],
    'leather': [1, 'В ней жарко и неудобно'],
    'tin': [2,'Такая себе, но на первое время хватит'],
    'copper': [2,'Защищает плохо, но красивая'],
    'gold': [3,'В глаза отсвечивает!'],
    'lead': [3,'Броня как броня'],
    'iron': [4,'В ней жарко, но хотябы защищает']
}
types_of_weapon = {
    'sword': [30,'Тяжелый но мощный'],
    'katana': [20, 'Легкая но хрупкая'],
}


def mod(name, points, type):
    if type == 'armor':
        return ModificationOfArmor(name, points)
    elif type == 'weapon':
        return ModificationOfWeapon(name, points)


armor_mods = [ModificationOfArmor(k, v) for k,v in modifications_of_armor.items()]
armor_types = [TypeOfArmor(k, *v) for k,v in types_of_armor.items()]
weapon_mods = [ModificationOfWeapon(k, v) for k, v in modifications_of_weapon.items()]
weapon_types = [TypeOfWeapon(k, *v) for k, v in types_of_weapon.items()]

characters = [
    Character("You"),
    Character("Enemy"),
]

characters[0].suite_armor(Armor("Megasuite", armor_types[-1]))
characters[1].suite_armor(Armor("Megaleather", armor_types[1]))

characters[0].hit("head")
characters[0].defence("head")
characters[1].defence("leg")
characters[1].hit("body")

print(characters[0] - characters[1])
print(characters[1] - characters[0])


armor_modifications = []
print("Armor mods:")
cnt = -1
for name, protect in modifications_of_armor.items():
    cnt += 1
    armor_modifications.append(mod(name, protect, "armor"))
    print(f'Name: "{name}", Protect points: "{protect}"; {armor_modifications[cnt]}')
