"""CSC 161 Lab: milestone 2

Ningyuan Xiong
Lab Section TR 12:30-1:45pm
Spring 2019
"""

def alg_moving_average(filename):
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
    cash_balance, stock_owned = before_last_day(lines)
    cash_balance = cash_balance + stock_owned * getprice(4634, lines)
    stock_owned = 0
    return stock_owned, cash_balance 

def before_last_day(lines):
    start_day = 1
    stock_owned = 0
    cash_balance = 1000
    while start_day != 4614:
        moving_average = average_20(start_day,lines)
        start_day = start_day + 1
        current_day = getprice(start_day + 19,lines)
        cash_balance, stock_owned = sell_buy(moving_average, current_day, stock_owned, cash_balance)
    return cash_balance, stock_owned

def sell_buy(moving_average, current_day, stock_owned, cash_balance):
    if moving_average + moving_average * 0.05 <= current_day:
        cash_balance, stock_owned = transact(cash_balance, stock_owned, current_day, buy = False, sell = True)
        return cash_balance, stock_owned
    elif moving_average - moving_average * 0.05 >= current_day:
        cash_balance, stock_owned = transact(cash_balance, stock_owned, current_day, buy = True, sell = False)
        return cash_balance, stock_owned
    else:
        return cash_balance, stock_owned

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

def average_20(start_day,lines):
    sum_ = 0
    for day in range(start_day,start_day+20):
        price = getprice(day,lines)
        sum_ = sum_ + price
    average_ = sum_ / 20
    return average_

def getprice(day,lines):
    row = lines[day]
    line = row.split(",")
    price = eval(line[4])
    return price

def main():
    filename = input("Enter a filename for stock data (CSV format): ")
    alg1_stocks, alg1_balance = alg_moving_average(filename)
    print("The results are {0:0.5f} cash balance and {1} stocks.".format(alg1_balance,alg1_stocks))


if __name__ == '__main__':
    main()

