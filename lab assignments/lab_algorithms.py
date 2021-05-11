"""CSC 161 Lab: Algorithms

Ningyuan Xiong
Lab Section TR 12:30-1:45pm
Spring 2019
"""

def sumlist(my_list):
    if len(my_list) == 0:
        return 0
    else:
        return my_list[0] + sumlist(my_list[1:])


def main():
    my_list = [7,5,4,27,52,42,13,17]
    Sumlist = sumlist(my_list)
    print(Sumlist)

main()
