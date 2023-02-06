import random

class Deck:
    def __init__(self):
        self.cards = []

        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

        ranks = [
            {"rank":"Ace","value":11},
            {"rank":"1","value":1},
            {"rank":"2","value":2},
            {"rank":"3","value":3},
            {"rank":"4","value":4},
            {"rank":"5","value":5},
            {"rank":"6","value":6},
            {"rank":"7","value":7},
            {"rank":"8","value":8},
            {"rank":"9","value":9},
            {"rank":"Jack","value":10},
            {"rank":"Queen","value":10},
            {"rank":"King","value":10},
            ]

        #loops through suits and ranks to build a deck of cards
        for suit in suits:
            n = len(ranks)-1
            while n > -1:
                self.cards.append([ranks[n],suit])
                n -=1

    #shuffles cards
    def shuffle(self):
        if len(self.cards)>1:
            random.shuffle(self.cards)

    #deals cards
    def deal(self,number_of_cards = 1):
        dealt_cards = []
        while number_of_cards > 0:
            if len(self.cards)>0:
                card = self.cards.pop()
                dealt_cards.append(card)
                number_of_cards -= 1
        return dealt_cards

deck1 = Deck()
deck2 = Deck()
deck2.shuffle()
# print(deck1.cards)
# print(deck2.cards)
deck2.deal(60)
