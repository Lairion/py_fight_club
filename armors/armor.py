class Armor:

    def __init__(self, name, armor_type):
        self.name = name
        self.armor_type = armor_type

    def hint(self):
        print(self.armor_type.hint)

    def add_modification(self, mod):
        if self.armor_type.type_of_armor == 'fabric': self.armor_type.protect_points = mod.protect_points
        else: self.armor_type.protect_points += mod.protect_points

    def protect_points_print(self):
        return self.armor_type.protect_points

    def __str__(self):
        return self.name
