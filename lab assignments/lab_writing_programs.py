'''CSC 161 Lab: Writing Simple Programs

Ningyuan Xiong
Lab Section: TR 1230-1345
Spring 2019
'''

def Main():
    print ("This function will take a mathematic expression and evaluate it.")
    for i in range(100):
        mathematic_expression = eval(input('Enter a mathematic expression: '))
        print (mathematic_expression)
Main()
