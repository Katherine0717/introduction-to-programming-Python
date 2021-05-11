"""CSC 161 Lab: milestone 3

Ningyuan Xiong
Lab Section TR 12:30-1:45pm
Spring 2019
"""

def alg_mine(filename): # Custom Algorithm
    """This function implements the student's custom trading algorithm.

    Using the CSV stock data that should be loaded into your program, use
    that data to make decisions using your own custome trading algorithm.

    Also, any bookkeeping setup in Milestone I should be called/used here.

    Args:
        A filename, as a string.

    Algorithm:
    - Trading starts on day 4, comparing to the past 3 days.
    - Buy shares if three days price before current day price is decreasing.
    - Sell shares if three days price before current day price is increasing.
    - Buy and sell 10 stocks per transaction.
    - Free to choose which column of stock data to use (open, close, low, high, etc)

    Returns:
        Two values, stocks and balance OF THE APPROPRIATE DATA TYPE.

    Prints:
        Nothing.
    """

    file = open(filename, 'r')
    lines = file.readlines()
    length = len(lines)
    # all balance and stock before the last day
    cash_balance, stocks_owned = before_last_day(lines,length)
    # plus last day balance and sell all the stocks
    cash_balance = cash_balance + stocks_owned * getprice(length-1, lines)
    stocks_owned = 0
    return stocks_owned, cash_balance 

def before_last_day(lines,length):
    start_day = 1
    stock_owned = 0
    cash_balance = 1000
    while start_day != length - 3 - 1:
        current_day = getprice(start_day + 3,lines)
        #check 3 days before current day
        # buy or sell stock
        if increase(start_day,lines,length) == True:
            cash_balance, stock_owned = transact(cash_balance, stock_owned, current_day, buy = True, sell = False)
        elif decrease(start_day,lines,length) == True:
            cash_balance, stock_owned = transact(cash_balance, stock_owned, current_day, buy = False, sell = True)
        start_day = start_day + 1
    return cash_balance, stock_owned

def decrease(start_day,lines,length):
    # check 3 days before current day are all decreasing
    price_min = getprice(start_day,lines)
    for i in range(start_day, start_day+3):
        price = getprice(i,lines)
        if price_min >= price:
            price_min = price
    if price_min == getprice(start_day+3,lines):
        return True

def increase(start_day,lines,x):
    # check 3 days before current day are all increasing
    price_max = getprice(start_day,lines)
    for i in range(start_day, start_day+3):
        price = getprice(i,lines)
        if price_max <= price:
            price_max = price
    if price_max == getprice(start_day+3,lines):
        return True


def transact(funds, stocks, price, buy=False, sell=False):
    if buy == True:
        funds_required = 10 * price
        if funds >= funds_required:
            funds = funds - funds_required
            stocks = stocks + 10
            return funds, stocks
        else:  
            return funds, stocks
    elif sell == True:
        if stocks >= 10:
            funds_required = 10 * price
            funds = funds + funds_required
            stocks = stocks - 10
            return funds, stocks
        else:
            return funds, stocks
    else:
        return funds, stocks

            
def getprice(day,lines):
    row = lines[day]
    line = row.split(",")
    price = eval(line[4])
    return price

def alg_moving_average(filename):# moving_average
    """This function implements the moving average stock trading algorithm.

    The CSV stock data should be loaded into your program; use that data to
    make decisions using the moving average algorithm.

    Any bookkeeping setup from Milestone I should be called/used here.

    Algorithm:
    - Trading must start on day 21, taking the average of the previous 20 days.
    - You must buy shares if the current day price is 5%, or more, lower than the moving average.
    - You must sell shares if the current day price is 5% higher, or more than the moving average.
    - You must buy, or sell 10 stocks per transaction.
    - You are free to choose which column of stock data to use (open, close, low, high, etc)

    Args:
        A filename, as a string.

    Returns:
        Two values, stocks and balance OF THE APPROPRIATE DATA TYPE.

    Prints:
        Nothing.
    """
    file = open(filename, 'r')
    lines = file.readlines()
    length = len(lines)
    cash_balance, stock_owned = before_last_day_(lines,length)
    cash_balance = cash_balance + stock_owned * getprice(length-1, lines)
    stock_owned = 0
    return stock_owned, cash_balance 

def before_last_day_(lines,length):
    start_day = 1
    stock_owned = 0
    cash_balance = 1000
    while start_day != length - 20 - 1:
        moving_average = average_20(start_day,lines)
        start_day = start_day + 1
        current_day = getprice(start_day + 19,lines)
        cash_balance, stock_owned = sell_buy_(moving_average, current_day, stock_owned, cash_balance)
    return cash_balance, stock_owned

def sell_buy_(moving_average, current_day, stock_owned, cash_balance):
    if moving_average + moving_average * 0.05 <= current_day:
        cash_balance, stock_owned = transact(cash_balance, stock_owned, current_day, buy = False, sell = True)
        return cash_balance, stock_owned
    elif moving_average - moving_average * 0.05 >= current_day:
        cash_balance, stock_owned = transact(cash_balance, stock_owned, current_day, buy = True, sell = False)
        return cash_balance, stock_owned
    else:
        return cash_balance, stock_owned


def average_20(start_day,lines):
    sum_ = 0
    for day in range(start_day,start_day+20):
        price = getprice(day,lines)
        sum_ = sum_ + price
    average_ = sum_ / 20
    return average_


def main():
    # My testing will use AAPL.csv or MSFT.csv
    filename = input("Enter a filename for stock data (CSV format): ")

    # Call your moving average algorithm, with the filename to open.
    alg1_stocks, alg1_balance = alg_moving_average(filename)

    # Print results of the moving average algorithm, returned above:
    print("The results of moving average are {0:0.5f} cash balance and {1} stocks.".format(alg1_balance, alg1_stocks))

    # Now, call your custom algorithm!
    alg2_stocks, alg2_balance = alg_mine(filename)

    # Print results of your algorithm, returned above:
    print("The results of mine are {0:0.5f} cash balance and {1} stocks.".format(alg2_balance, alg2_stocks))

if __name__ == '__main__':
    main()
