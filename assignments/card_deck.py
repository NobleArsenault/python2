import random
class cards(object):
    def __init__(self):
        self.suit = ["diamonds", "clubs", "hearts", "spades"]
        self.value = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
        self.deck = []
    def createCards(self):
        for i in self.suit:
            for j in self.value:
                self.deck.append(j + " of " + i )
        return self
    def __repr__(self):
        return "{}".format(self.deck[0])

    def shuffle(self):
        random.shuffle(self.deck)
        return self
    def dealCard(self):
        print self.deck[0]
        return self
    def displayDeck(self):
        print self.deck
        return self



nobleCards = cards()
nobleCards.createCards().shuffle().dealCard()