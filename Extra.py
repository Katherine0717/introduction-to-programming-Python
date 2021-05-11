"""CSC 161 Lab: extra credit

Ningyuan Xiong
Lab Section TR 12:30-1:45pm
Spring 2019
"""

# object-oriented design for moving average algorithm:
def main():
    import math
    filename = "AAPL.csv"
    file = open(filename, 'r')
    lines = file.readlines()
    length = len(lines)

    # all balance gained and stocks before last day:
    trading_ = trading()
    GetValue = getValue()
    Sell_Buy = SellBuy()
    for i in range(21,length):
        Sell_Buy.average(GetValue,lines)
        Sell_Buy.update(trading_,GetValue,lines)
    cash_balance, stock_owned = trading_.gets()

    # add up to the last day price, and sell all the stocks
    cash_balance = cash_balance + stock_owned * GetValue.getprice(length-1, lines)
    stock_owned = 0
    print("1. Object-oriented design:")
    print("   The results are {0:0.5f} cash balance and {1} stocks.".format(cash_balance,stock_owned))
    print(" ")
    print(" ")
    print("3. Statistics:")
    print("   Comparing alg_mine and alg_moving_average, calculating previous 20 days' prices to")
    print("   determined buying or selling is a better way. Mine algorithm only considered whether")
    print("   previous 3 days prices are increasing or decreasing. However, I didn't consider if")
    print("   all three-day-price are increasing but it's increasing more slowly. If compareing")
    print("   whether the current day price is 5%, or more, lower than the moving average, it will")
    print("   obtain more in the total balance.")

    



class SellBuy:
    def __init__(self):
        self.start_day = 1
        self.price = 0
        self.current_day = 0
                
    def average(self,GetValue,lines):
        sum_ = 0
        for day in range(self.start_day, self.start_day + 20):
            price = GetValue.getprice(day, lines)
            sum_ = sum_ + price
        self.average_ = float(sum_ / 20)

    def update(self,trading,getValue,lines):
        self.current_day = getValue.getprice(self.start_day + 20,lines)
        self.start_day = self.start_day + 1
        x = self.average_ + self.average_ * 0.05
        y = self.average_ - self.average_ * 0.05
        if x <= self.current_day: #SELL
            trading.sell(self.current_day)
            
        elif y >= self.current_day:#BUY
            trading.buy(self.current_day)
            

class getValue:
    def __init__(self):
        self.price = 0
        
    def getprice(self,start_day,lines):
        row = lines[start_day]
        line = row.split(",")
        self.price = eval(line[4])
        return self.price

        
class trading:
    buy_stock = 10
    sell_stock = 10
    def __init__(self):
        self.balance = 1000
        self.stock = 0

    def sell(self,price):
        if self.stock >= self.sell_stock:
            self.balance = self.balance + self.sell_stock * price
            self.stock = self.stock - self.sell_stock

    def buy(self,price):
        if self.balance >= self.sell_stock * price:
            self.balance = self.balance - self.buy_stock * price
            self.stock = self.stock + self.buy_stock

    def gets(self):
        return self.balance, self.stock

        
if __name__ == '__main__':
    main()




