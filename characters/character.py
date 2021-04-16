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

    def check_damage(self, other):
        if self.hited == other.defenced:
            return self.damage_dict[self.hited] - other.defence_dict[other.defenced]
        return self.damage_dict[self.hited]

    def __str__(self):
        return f"Name:{self.name} Armor:{self.armor} hp:{self.hp}"

    def __sub__(self, other):
        other.hp = other.hp - self.check_damage(other)
        return (str(self), str(other))
