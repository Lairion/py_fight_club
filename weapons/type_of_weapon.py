class TypeOfWeapon:

    def __init__(self, name, damage, hint):
        self.name = name
        self.damage = damage
        self.hint = hint

    def __str__(self):
        return self.name
