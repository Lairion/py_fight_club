class Character:

    types_of_armor = {
        'fabric': [0, 'На такую нельзя надеется...'],
        'leather': [1, 'В ней жарко и неудобно'],
        'tin': [2, 'Такая себе, но на первое время хватит'],
        'copper': [2, 'Защищает плохо, но красивая'],
        'gold': [3, 'В глаза отсвечивает!'],
        'lead': [3, 'Броня как броня'],
        'iron': [4, 'В ней жарко, но хотябы защищает']
    }

    hp = 100

    bonus_damage_dict = {
        "head": 5,
        "hand": 1,
        "body": 3,
        "leg": 1
    }

    attacked_part_of_body = 0
    defenced_part_of_body = 0

    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def hit(self, part_of_body):
        self.attacked_part_of_body = part_of_body

    def defence(self, part_of_body):
        self.defenced_part_of_body = part_of_body

    def suite_armor(self, armor):
        self.armor = armor

    def take_weapon(self, weapon):
        self.weapon = weapon

    def check_damage(self, other):
        if self.attacked_part_of_body != other.defenced_part_of_body:
            damage = self.weapon.damage * self.bonus_damage_dict[self.attacked_part_of_body]\
                     - other.armor.protection_points
            if damage < 0:
                return 0
            return damage
        return self.weapon.damage - self.armor.protection_points

    def __str__(self):
        return f'{self.name}: Armor = "{self.armor.type_of_armor.capitalize()}", Armor protect points = ' \
               f'"{self.armor.protection_points}", Weapon = "{self.weapon.name.capitalize()}", Weapon damage = "' \
               f'{self.weapon.damage}", HP = "{self.hp}"'

    def __sub__(self, other):
        other.hp = other.hp - self.check_damage(other)
        return str(self) + '\n' + str(other) + '\n-=-=-=-=-\n'
