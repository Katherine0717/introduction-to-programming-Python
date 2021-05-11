"""CSC 161 Lab: Classes
 
Ningyuan Xiong
Lab Section TR 12:30-1:45pm
Spring 2019
"""

class PlayingCard:
    def __init__(self,rank,suit):
        self.rank = int(rank)
        self.suit = suit

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def bj_value(self):
        if self.rank == 11 or self.rank == 12 or self.rank == 13:
            return 10
        else:
            return self.rank


    def __repr__(self):
        if self.suit == "d":
            self.suit2 = "Diamond"
        elif self.suit == "c":
            self.suit2 = "Clubs"
        elif self.suit == "h":
            self.suit2 = "Hearts"
        else:
            self.suit2 = "Spades"
        String = "Ace,Two,Three,Four,Five,Six,Seven,Eight,Nine,Ten,Jack,Queen,King"
        String1 = String.split(",")
        self.rank2 = String1[self.rank-1]
    
        s = "{0} of {1}".format(self.rank2,self.suit2)
        return s

def main():
    import random
    print("Testing card class")
    n = eval(input(("How many cards would you like to see?")))
    playcard = PlayingCard(13,4)
    x = 0
    while x != n:
        x = x + 1
        s = random.randrange(1,5)
        rank = random.randrange(1,14)
        if s == 1:
            suit = "d"
        elif s == 2:
            suit = "h"
        elif s == 3:
            suit = "c"
        else:
            suit = "s"
        C = PlayingCard(rank,suit)
        print(C)


    
        
    
        
