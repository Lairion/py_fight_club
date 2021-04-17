class Armor:

    def __init__(self, name, armor_type):
        self.name = name
        self.armor_type = armor_type
        # print('The armor is initialized.',"Type:", self.armor_type.type_of_armor)

    def hint(self):
        print(self.armor_type.hint)

    def __str__(self):
        return self.name
