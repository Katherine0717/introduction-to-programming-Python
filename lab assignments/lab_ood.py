"""CSC 161 Lab: Object-Oriented Design

Ningyuan Xiong
Lab Section TR 12:30-1:45pm
Spring 2019
"""

def main():
    fakeacc = {"JSmith": 3000, "KGreen": 3200, "SRobert": 5000, "WLee": 1250}
    fakePin = {"12345": "JSmith", "23456": "KGreen", "34567": "SRobert", "45678": "WLee"}
    ID_ = ID(fakeacc)
    Pin = pin(fakePin)
    balance = fakeacc.get(ID_, "There is no such account.")
    C = CheckAccount(balance)
    print("Your account balance:", C.getbalance())
    X = input("Do you want to deposit or withdraw?(deposit: +/ withdraw: -)")
    M = eval(input("Enter the amount of money:"))
    if X == "+":
        C.deposit(M)
        print("Your account balance:", C.getbalance())
    elif X == "-":
        C.withdrawl(M)
        print("Your account balance:", C.getbalance())
        
        
    
    

def pin(fakePin):
    pin = input("Please enter your PIN number:")
    while True:
        X = pin in fakePin
        if X == True:
            break
        else:
            print("Your PIN number is not correct.")
            pin = input("Please enter your PIN number:")
    return pin

def ID(fakeacc):
    ID = input("Please enter your ID:")
    while True:
        Y = ID in fakeacc
        if Y == True:
            break
        else:
            print("Your ID number is not correct.")
            ID = input("Please enter your ID number:")
    return ID

    
class CheckAccount:
    def __init__(self,balance):
        self.balance = int(balance)

    def getbalance(self):
        return self.balance

    def withdrawl(self,value):
        if value >= self.balance:
            self.balance = self.balance - value
        else:
            print("You don't have enough money.")

    def deposit(self,value):
        self.balance = self.balance + value
    

main()
