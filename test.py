import json

player = {
    'armor_type' : 1,
    'armor_mod'  : 1,
    'armor_name' : 'Iron',
    'weapon_type': 0,
    'weapon_mod' : 3,
    'weapon_name': 'Sword',
    'hand_coeff' : 1
}

with open('data.txt', 'w') as outfile:
    json.dump(player, outfile)

with open('data.txt') as json_file:
    data = json.load(json_file)
    print(data)
    [print(f'{key}: {value}') for key, value in data.items()]
