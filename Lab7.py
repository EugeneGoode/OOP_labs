import random as r

print(9210 % 2)
print(9210 % 3)

collection = list()


class Armor:
    body_part_list = ['Chest', 'Head', 'Forearms', 'Legs']

    def __init__(self, body_part, protection = 0, price = 0, weight = 0):
        self.body_part = body_part
        self.protection = protection
        self.price = price
        self.weight = weight


class Knight:
    def __init__(self, chest_piece = None, helmet = None, forearm_piece = None, leg_piece = None):
        if chest_piece != None:
            self.chest_piece = chest_piece
        if helmet != None:
            self.helmet = helmet
        if forearm_piece != None:
            self.forearm_piece = forearm_piece
        if leg_piece != None:
            self.leg_piece = leg_piece

    def equip_existing(self, armor):
        print(armor.body_part, 'is/are protected')
        if armor.body_part == 'Chest':
            self.chest_piece = Armor(armor.body_part, armor.protection, armor.price, armor.weight)
        elif armor.body_part == 'Head':
            self.helmet = Armor(armor.body_part, armor.protection, armor.price, armor.weight)
        elif armor.body_part == 'Forearms':
            self.forearm_piece = Armor(armor.body_part, armor.protection, armor.price, armor.weight)
        elif armor.body_part == 'Legs':
            self.leg_piece = Armor(armor.body_part, armor.protection, armor.price, armor.weight)


    def equip(self, body_part = 'Head', protection = 3, price = 100, weight = 5):
        print(body_part, 'is/are protected')
        Armor(body_part, protection, price, weight)
        if body_part == 'Chest':
            self.chest_piece = Armor(body_part, protection, price, weight)
        if body_part == 'Head':
            self.helmet = Armor(body_part, protection, price, weight)
        if body_part == 'Forearms':
            self.forearm_piece = Armor(body_part, protection, price, weight)
        if body_part == 'Legs':
            self.leg_piece = Armor(body_part, protection, price, weight)

    def equip_collection(self):
        for i in collection:
            if i.body_part == 'Chest':
                self.chest_piece = Armor(i.body_part, i.protection, i.price, i.weight)
            elif i.body_part == 'Head':
                self.helmet = Armor(i.body_part, i.protection, i.price, i.weight)
            elif i.body_part == 'Forearms':
                self.forearm_piece = Armor(i.body_part, i.protection, i.price, i.weight)
            elif i.body_part == 'Legs':
                self.leg_piece = Armor(i.body_part, i.protection, i.price, i.weight)

for i in range(15):
    collection.insert(i, Armor(Armor.body_part_list[r.randint(0, 3)], r.randint(1, 10), r.randint(1, 5000),r.randint(1, 20)))

for i in range(20):
    collection.insert(i, Armor(Armor.body_part_list[r.randint(0, 3)], r.randint(1, 10), r.randint(1, 5000),r.randint(1, 20)))

John = Knight()
John.equip_existing(collection[3])
John.equip_collection()