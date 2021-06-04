class TypeOfArmor:

    def __init__(self, type_of_armor, protect_points, hint):
        self.type_of_armor = type_of_armor
        self.protect_points = protect_points
        self.hint = hint
        self.hp = 0

    def __str__(self):
        return self.type_of_armor
