"""CSC 161 Lab: Loops & Booleans

Ningyuan Xiong
Lab Section TR 12:30-1:45pm
Spring 2019
"""

def get_input():
    import math
    while True:
        while True:
            try:
                number =eval(input("Please enter an even integer larger than 2: "))
            except NameError:
                print ("Bad Input!")
            else:
                break
        if number % 2 == 1 or number <=2:
            print ("Wrong Input!")
        else:
            break
    return number

def is_prime(n):
    i = 2
    while i < n/2:
        if n % i != 0:
            i += 1
        else:
            return False
            break
    return True

def main():
    num = get_input()
    for n in range(1, num):
        if is_prime(n) == True:
            if is_prime(num-n) == True:
                print(num,"=",n,"+",num-n)
                break

main()
