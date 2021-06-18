class Character:

    weapon = None
    armor = None
    damage = 10
    hp = 100

    damage_dict = {
        "head": 50,
        "body": 30,
        "leg": 10,
        "hand": 10,
    }

    defenced = None
    attacked = None

    def __init__(self, name):
        self.name = name

    def hit(self, part_of_body):
        self.attacked = part_of_body

    def defence(self, part_of_body):
        self.defenced = part_of_body

    def suite_armor(self, armor):
        self.armor = armor

    def take_weapon(self, weapon):
        self.weapon = weapon

    def calc_damage(self):
        if self.weapon:
            return self.weapon.hit(self.damage_dict[self.attacked])
        return self.damage_dict[self.attacked]

    def calc_defence(self):
        if self.armor:
            return self.armor.armor_type.protect_points
        return 0

    def check_damage(self, other):
        damage = self.calc_damage()

        if self.attacked == other.defenced:
            damage -= other.damage_dict[other.defenced]
        damage -= other.calc_defence()
        print(damage)
        if damage < 0:
            return 0
        return damage

    def __str__(self):
        return f'{self.name}: ' \
               f'HP = "{self.hp}"; ' \
               f'Armor = "{self.armor.name}" ({self.armor.protect_points_print()} def. points); ' \
               f'Weapon = "{self.weapon.name}" ({self.weapon.full_damage} damage); ' \
               f'Attacked part of body: "{self.attacked}"; ' \
               f'Defenced part of body: "{self.defenced}".'

    def __sub__(self, other):
        # -

        other.hp = other.hp - self.check_damage(other)
        if other.hp < 0: other.hp = 0
        return self

    def __gt__(self,other):
        if isinstance(other,int):
            other_hp = other
        else:
            other_hp = other.hp
        if self.hp > other_hp:
            return self
        elif self.hp == other_hp:
            return None
        return other
    # return biggest Character


    def __lt__(self,other):
        if self.hp < other.hp:
            return self
        elif self.hp == other.hp:
            return None
        return other
    #return smallest Character
