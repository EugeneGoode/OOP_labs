print(9210 % 13)


class Armor:
    def __init__(self, body_part, protection = 0, price = 0, weight = 0):
        self.body_part = body_part
        self.protection = protection
        self.price = price
        self.weight = weight
        if body_part == 'Chest':
            self.chest_piece = ChestPiece(protection, price, weight)
        if body_part == 'Head':
            self.helmet = Helmet(protection, price, self.weight)
        if body_part == 'Forearms':
            self.forearm_piece = ForearmPiece(protection, price, weight)
        if body_part == 'Legs':
            self.leg_piece = LegPiece(protection, price, weight)


class Knight(Armor):
    total = 0
    prices = []
    weights = []
    piece_list = []
    def __init__(self, chest_piece = None, helmet = None, forearm_piece = None, leg_piece = None):
        if chest_piece != None:
            self.chest_piece = chest_piece
            self.piece_list.append(chest_piece)
        if helmet != None:
            self.helmet = helmet
            self.piece_list.append(helmet)
        if forearm_piece != None:
            self.forearm_piece = forearm_piece
            self.piece_list.append(forearm_piece)
        if leg_piece != None:
            self.leg_piece = leg_piece
            self.piece_list.append(leg_piece)

    def equip_existing(self, armor):
        print(armor.body_part, 'is/are protected')
        if armor.body_part == 'Chest':
            self.chest_piece = Armor(armor.body_part, armor.protection, armor.price, armor.weight)
            self.piece_list.append(self.chest_piece)
        elif armor.body_part == 'Head':
            self.helmet = Armor(armor.body_part, armor.protection, armor.price, armor.weight)
            self.piece_list.append(self.helmet)
        elif armor.body_part == 'Forearms':
            self.forearm_piece = Armor(armor.body_part, armor.protection, armor.price, armor.weight)
            self.piece_list.append(self.forearm_piece)
        elif armor.body_part == 'Legs':
            self.leg_piece = Armor(armor.body_part, armor.protection, armor.price, armor.weight)
            self.piece_list.append(self.leg_piece)

    def equip(self, body_part = 'Head', protection = 3, price = 100, weight = 5):
        print(body_part, 'is/are protected')
        Armor(body_part, protection, price, weight)
        if body_part == 'Chest':
            self.chest_piece = Armor(body_part, protection, price, weight)
            self.piece_list.append(self.chest_piece)
        if body_part == 'Head':
            self.helmet = Armor(body_part, protection, price, weight)
            self.piece_list.append(self.helmet)
        if body_part == 'Forearms':
            self.forearm_piece = Armor(body_part, protection, price, weight)
            self.piece_list.append(self.forearm_piece)
        if body_part == 'Legs':
            self.leg_piece = Armor(body_part, protection, price, weight)
            self.piece_list.append(self.leg_piece)

    def price_operation(self, price_range = (1, 1000)):
        for i in self.piece_list:
            self.prices.append(i.price)
            self.total += i.price
            if i.price in range(price_range[0], price_range[1]):
                print(i.body_part, 'задовольняє діапазон цін')
        print('Загальна вартість: ', self.total)

    def weight_operation(self):
        print('Амуніція відсортована за вагою: ')
        for i in self.piece_list:
            self.weights.append(i.weight)
        self.weights.sort()
        for s in self.weights:
            for q in self.piece_list:
                if q.weight == s:
                   print(q.body_part, 'з вагою', s)


class ChestPiece(Armor):
    def __init__(self, protection, price, weight):
        super().__init__(protection, price, weight)


class Helmet(Armor):
    def __init__(self, protection, price, weight):
        super().__init__(protection, price, weight)


class ForearmPiece(Armor):
    def __init__(self, protection, price, weight):
        super().__init__(protection, price, weight)


class LegPiece(Armor):
    def __init__(self, protection, price, weight):
        super().__init__(protection, price, weight)


NewHelmet = Armor('Head', 7, 300, 10)
John = Knight(helmet=NewHelmet)
John.equip('Chest', 10, 500, 20)
John.equip('Forearms', 5, 150, 5)
John.equip('Legs', 8, 500, 15)
John.price_operation()
John.weight_operation()


