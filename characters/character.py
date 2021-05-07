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
    defence_dict = {
        "head": 50,
        "body": 30,
        "leg": 10,
        "hand": 10,
    }
    defenced = None
    hited = None

    def __init__(self, name):
        self.name = name

    def hit(self, part_of_body):
        self.hited = part_of_body

    def defence(self, part_of_body):
        self.defenced = part_of_body

    def suite_armor(self, armor):
        self.armor = armor

    def take_weapon(self, weapon):
        self.weapon = weapon

    def calc_damage(self):
        if self.weapon:
            return self.weapon.hit(self.damage_dict[self.hited])
        return self.damage_dict[self.hited]

    def calc_defence(self):
        if self.armor:
            return self.armor.defence_point()
        return 0

    def check_damage(self, other):
        damage = self.calc_damage()
        if self.hited == other.defenced:
            damage -= other.defence_dict[other.defenced]
        damage -= other.calc_defence()
        if damage < 0:
            return 0
        return damage

    def __str__(self):
        return f'{self.name}: HP = "{self.hp}",\nArmor = "{self.armor.name}",\nHited part of body: ' \
              f'"{self.hited}",\nDefenced part of body: "{self.defenced}"'

    def __sub__(self, other):
        other.hp = other.hp - self.check_damage(other)
        if other.hp < 0: other.hp = 0
        return str(self)
