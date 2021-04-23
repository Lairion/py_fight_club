class Weapon:
    def __init__(self, name, damage, hand_coef):
        self.name = name
        self.damage = damage
        self.hand_coef = hand_coef

    def hit(self, damage):
        return damage // self.hand_coef + damage

    def add_modification(self, mod):
        pass
