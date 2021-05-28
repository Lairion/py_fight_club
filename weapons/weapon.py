class Weapon:

    modifications = []

    def __init__(self, name, type_of_weapon, hand_coef):
        self.name = name
        self.weapon_type = type_of_weapon
        self.full_damage = type_of_weapon.damage
        self.hand_coef = hand_coef

    def hit(self, damage):
        return damage // self.hand_coef + self.full_damage

    def add_modification(self, mod):
        self.full_damage += mod.damage
        self.modifications.append(mod)

    def characteristic_of_modification(self):
        return {i.name: i.damage for i in self.modifications}

    def __str__(self):
        return f"Name of weapon :{self.name} Hit:{self.full_damage} Modification:{self.modifications} Type of weapon: {self.weapon_type}"
