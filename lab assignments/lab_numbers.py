"""CSC 161 Lab: Numbers

Ningyuan Xiong
Lab Section: TR 1230-1345
Spring 2019
"""

import math
def main():
	print("This program calculate the squre root of a given number using the Newton's method.")
	x = eval(input("What is the number for which you want to calculate the squre root?"))
	iteration = eval(input("How many iterations do you want to use?"))
	print("My guess for the square root of",x,"is", math.sqrt(x))
	guess = x/2
	discRoot = math.sqrt(x)
	for i in range(0,iteration):
		guess = (guess + (x/guess))/2
		difference = guess - discRoot
	print("The difference between my guess and the real result is", difference)

main()
