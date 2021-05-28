class Weapon:

    modification = None

    def __init__(self, name, type_of_weapon, hand_coef):
        self.name = name
        self.weapon_type = type_of_weapon
        self.full_damage = type_of_weapon.damage
        self.hand_coef = hand_coef

    def hit(self, damage):
        return damage // self.hand_coef + self.full_damage

    def add_modification(self, mod):
        self.full_damage += mod.damage
        self.modification = mod.name

    def __str__(self):
        return f'Name: "{self.name}";\n' \
               f'Damage: "{self.full_damage}";\n' \
               f'Modification: "{self.modification}";\n' \
               f'Type: "{self.weapon_type}".'
