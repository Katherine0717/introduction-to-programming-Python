"""CSC 161 Lab: Data Collections

Ningyuan Xiong
Lab Section TR 12:30-1:45pm
Spring 2019
"""
from random import randrange
from lab_classes import PlayingCard
from math import sqrt

suit_size = 13  # Number of cards in a suit.
deck_size = 52  # Number of cards in a deck.
num_cards = 260  # Number of cards to create with random rank & suit values


def make_random_cards():
    """Generate num_cards number of random PlayingCard objects.

    This function will generate num_cards RANDOM playing cards
    using your PlayingCard class. That means you will have to choose a random
    suit and rank for a card num_cards times.

    Printing:
        Nothing

    Positional arguments:
        None

    Returns:
        cards_list -- a list of PlayingCard objects.
    """

    num_cards = randrange(1,261)
    x = 0
    cards_list=[]
    while x != num_cards:
        x = x + 1
        s = randrange(1,5)
        rank = randrange(1,14)
        if s == 1:
            suit = "d"
        elif s == 2:
            suit = "h"
        elif s == 3:
            suit = "c"
        else:
            suit = "s"
        C = PlayingCard(rank,suit)
        cards_list.append(C)
    return cards_list


def freq_count(cards_list):
    """Count every suit-rank combination.

    Returns a dictionary whose keys are the card suit-rank and value is the
    count.

    Printing:
        Nothing

    Positional arguments:
        cards_list -- A list of PlayingCard objects.

    Returns:
        card_freqs -- A dictionary whose keys are the single letter in the set
        'd', 'c', 'h', 's' representing each card suit.  The value for each key
        is a list containing the number of cards at each rank, using the index
        position to represent the rank. For example, {'s': [0, 3, 4, 2, 5]}
        says that the key 's', for 'spades' has three rank 1's (aces), four
        rank 2's (twos), two rank 3's (threes) and 5 rank 4's (fours).  Index
        position 0 is 0 since no cards have a rank 0, so make note.
    """
    # DO NOT REMOVE BELOW
    if type(cards_list) != list or \
            list(filter(lambda x: type(x) != PlayingCard, cards_list)):
        raise TypeError("cards_list is required to be a list of PlayingCard \
                        objects.")
    # DO NOT REMOVE ABOVE
    
    card_freqs = {"s": [0]*14, "d": [0]*14, "h" : [0]*14, "c" : [0]*14}
    for card in cards_list:
        card_freqs[card.suit][card.rank]+= 1
    return card_freqs
   
    
def std_dev(counts):
    """Calculate the standard deviation of a list of numbers.

    Positional arguments:
        counts -- A list of ints representing frequency counts.

    Printing:
        Nothing

    Returns:
        _stdev -- The standard deviation as a single float value.
    """
    # DO NOT REMOVE BELOW
    if type(counts) != list or \
            list(filter(lambda x: type(x) != int, counts)):
        raise TypeError("counts is required to be a list of int values.")
    # DO NOT REMOVE ABOVE

    _sum = 0.0
    for i in counts:
        _sum = _sum + i
    _mean = _sum/13
    _stdev = 0.0
    for x in counts:
        dev = _mean - x
        _stdev = _stdev + dev * dev
    _stdev_ = sqrt(_stdev/12)
    return _stdev_


def print_stats(card_freqs):
    """Print the final stats of the PlayingCard objects.

    Positional arguments:
        card_freqs -- A dictionary whose keys are the single letter in the set
        'dchs' representing each card suit. The value for each key is a list of
        numbers where each index position is a card rank, and its value is its
        card frequency.

        You will probably want to call th std_dev function in somewhere in
        here.

    Printing:
        Prints the statistic for each suit to the screen, see assignment page
        for an example output.

    Returns:
        None
    """
    # DO NOT REMOVE BELOW
    if type(card_freqs) != dict or \
            list(filter(lambda x: type(card_freqs[x]) != list, card_freqs)):
        raise TypeError("card_freqs is required to be a dict where each value is a list of ints.")
    # DO NOT REMOVE ABOVE

    sd_s = std_dev(card_freqs["s"])
    sd_d = std_dev(card_freqs["d"])
    sd_c = std_dev(card_freqs["c"])
    sd_h = std_dev(card_freqs["h"])
    print("Standard deviation for the frequency counts of each rank in suit:")
    print("Hearts: {0:0.4f} cards".format(sd_h))
    print("Spades: {0:0.4f} cards".format(sd_s))
    print("Clubs: {0:0.4f} cards".format(sd_c))
    print("Diamonds: {0:0.4f} cards".format(sd_d))

def main():
    cards = make_random_cards()
    suit_counts = freq_count(cards)
    print_stats(suit_counts)
    
if __name__ == "__main__":
    main()
