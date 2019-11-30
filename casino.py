import random
# Card Value
# 1: Ac
# 2 - 10: 2 - 10
# 11: Jack
# 12: Queen
# 13: King
# Suits
# H: Hearts
# D: Diamonds
# C: Clubs
# S: Spades
class cards:
    def __init__(self):
        self.AllCards = []
        for n in range(1,14):
            card = n
            cardtype = ''
            for i in range(3):
                if i == 0:
                    cardtype = 'H'
                elif i == 1:
                    cardtype = 'D'
                elif i == 2:
                    cardtype = 'C'
                elif i == 3:
                    cardtype = 'S'
            self.AllCards.append([card, cardtype])
        self.AllCards = self.AllCards * 6
    def getCards(self):

        return self.AllCards
class dealer:
    def __init__(self, c):
        self.curvalue = 0
        self.cardsl = c
        self.dealercards = []

    def deal(self):
        r1 = random.randint(0, len(self.cardsl)-1)
        randcard = self.cardsl[r1]
        self.cardsl.pop(r1)
        self.dealercards.append(randcard)

        r2 = random.randint(0, len(self.cardsl) - 1)
        randcard2 = self.cardsl[r2]
        self.cardsl.pop(r2)
        self.dealercards.append(randcard2)

        self.situation()
        return self.dealercards

    def situation(self):
        points = 0
        if self.dealercards[0][0] == 1 and self.dealercards[1][0] == 1:
            points += 12
        else:
            if self.dealercards[0][0] == 11 or self.dealercards[0][0] == 12 or self.dealercards[0][0] == 13:
                points += 10
            else:
                points += self.dealercards[0][0]
            if self.dealercards[1][0] == 11 or self.dealercards[1][0] == 12 or self.dealercards[1][0] == 13:
                points += 10
            else:
                points += self.dealercards[1][0]
        self.curvalue = points

        if points == 11 and(self.dealercards[0][0] == 1 or self.dealercards[1][0] == 1):
            self.curvalues = 21
            return self.curvalue
        elif points < 17:
            self.hit()
        else:
            return self.curvalue

    def hit(self):
        points = 0
        rand = random.randint(0, len(self.cardsl) - 1)
        card = self.cardsl[rand]
        self.dealercards.append(card)
        self.cardsl.pop(rand)

        if card[0] == 11 or card[0] == 12 or card[0] == 13:
            points = 10
        elif card[0] == 1 and self.curvalue < 11:
            points = 11
        elif card[0] == 1 and self.curvalue == 20:
            points = 1
        else:
            points = card[0]

        self.curvalue += points
        if self.curvalue < 17:
            self.hit()
        elif self.curvalue > 21:
            return self.curvalue
        else:
            return self.curvalue

    def getScore(self):
        return self.curvalue

    def reset(self):
        self.dealercards = []
        self.curvalue = 0


class player:

    def __init__(self, AllCards):
        self.AllCards = AllCards
        self.PlayerCards = []
        self.curValue = 0

    def deal(self):

        n1 = random.randint(0, len(self.AllCards) - 1)
        self.PlayerCards.append(self.AllCards[n1])
        self.AllCards.pop(n1)
        n2 = random.randint(0, len(self.AllCards) - 1)
        self.PlayerCards.append(self.AllCards[n2])
        self.AllCards.pop(n2)

        #self.AllCards = self.AllCards

        sum_of_cards = 0
        if self.PlayerCards[0][0] == 1 and self.PlayerCards[1][0] == 1:
            sum_of_cards += 12
        else:
            if self.PlayerCards[0][0] == 11 or self.PlayerCards[0][0] == 12 or self.PlayerCards[0][0] == 13:
                sum_of_cards += 10
            else:
                sum_of_cards += self.PlayerCards[0][0]
            if self.PlayerCards[1][0] == 11 or self.PlayerCards[1][0] == 12 or self.PlayerCards[1][0] == 13:
                sum_of_cards += 10
            else:
                sum_of_cards += self.PlayerCards[1][0]
            self.curValue = sum_of_cards
            if sum_of_cards == 11 and (self.PlayerCards[0][0] == 1 or self.PlayerCards[1][0] == 1):   #Think as an error.
                self.curValue = 21
        return self.PlayerCards

    def hit(self):
        value = 0
        n3 = random.randint(0, len(self.AllCards) - 1)
        hitcard = self.AllCards[n3]
        self.PlayerCards.append(self.AllCards[n3])
        self.AllCards.pop(n3)
        if hitcard[0] == 1 and self.curValue < 11:
            value = 11
        elif hitcard[0] == 11 or hitcard[0] == 12 or hitcard[0] == 13:
            value = 10
        else:
            value = hitcard[0]
        self.curValue += value
        if self.curValue > 21 and self.PlayerCards.__contains__(1):
            if self.PlayerCards.count(1) == 1:
                if self.curValue - 10 < 22:
                    self.curValue = self.curValue - 10
        return hitcard

    def getScore(self):
        return self.curValue

