"""CSC 161 project: Milestone 1

Ningyuan Xiong
Lab Section TR 12:30-1:45pm
Spring 2019
"""
def test_data(filename, col, day):
    """A test function to query the data you loaded into your program.

    Args:
        filename: A string for the filename containing the stock data,
                  in CSV format.

        col: A string of either "date", "open", "high", "low", "close",
             "volume", or "adj_close" for the column of stock market data to
             look into.

             The string arguments MUST be LOWERCASE!

        day: An integer reflecting the absolute number of the day in the
             data to look up, e.g. day 1, 15, or 1200 is row 1, 15, or 1200
             in the file.

    Returns:
        A value selected for the stock on some particular day, in some
        column col. The returned value *must* be of the appropriate type,
        such as float, int or str.
    """
    file = open(filename, 'r')
    lines = file.readlines()
    row = lines[day]
    line = row.split(",")
    Open = float(line[1])   
    High = float(line[2])
    Low = float(line[3])
    close = float(line[4])
    Adj_Close = float(line[5])
    Volume = float(line[6])
    if col in ["Open","open"]:
        return Open
    elif col in ["High","high"]:
        return High
    elif col in ["Low","low"]:
        return Low
    elif col in ["close","Close"]:
        return close
    elif col in ["Adj Close", "adj close"]:
        return Adj_Close
    elif col in ["volume","Volume"]:
        return Volume
    else:
        print("There is no such column.")

def main():
    pass

if __name__ == '__main__':
    main()

def transact(funds, stocks, qty, price, buy=False, sell=False):
    """A bookkeeping function to help make stock transactions.

       Args:
           funds: An account balance, a float; it is a value of how much money you have,
                  currently.

           stocks: An int, representing the number of stock you currently own.

           qty: An int, representing how many stock you wish to buy or sell.

           price: An float reflecting a price of a single stock.

           buy: This option parameter, if set to true, will initiate a buy.

           sell: This option parameter, if set to true, will initiate a sell.

       Returns:
           Two values *must* be returned. The first (a float) is the new
           account balance (funds) as the transaction is completed. The second
           is the number of stock now owned (an int) after the transaction is
           complete.

           Error condition #1: If the `buy` and `sell` keyword parameters are both set to true,
           or both false. You *must* print an error message, and then return
           the `funds` and `stocks` parameters unaltered. This is an ambiguous
           transaction request!

           Error condition #2: If you buy, or sell without enough funds or
           stocks to sell, respectively.  You *must* print an error message,
           and then return the `funds` and `stocks` parameters unaltered. This
           is an ambiguous transaction request!
    """
    
    if buy == False and sell == False:
        print("Ambigious transaction! Can't determine whether to buy or sell. No action performed.")
        return cash_balance, stocks_owned
    elif buy == True and sell == True:
        print("Ambigious transaction! Can't determine whether to buy or sell. No action performed.")
        return cash_balance, stocks_owned
    elif buy == "" and sell == "":
        print("Ambigious transaction! Can't determine whether to buy or sell. No action performed.")
        return cash_balance, stocks_owned
    elif buy == True:
        funds_required = qty * price
        if funds >= funds_required:
            new_funds = funds - funds_required
            new_stocks = stocks + qty
            return new_funds, new_stocks
        else:
            print("Insufficient funds: purchase of",qty,"at ${0:0.2f} requires {1}, but ${2} available!".format(price,funds_required,funds))
            return cash_balance, stocks_owned
    elif sell == True:
        if stocks >= qty:
            funds_required = qty * price
            new_funds = funds + funds_required
            new_stocks = stocks - qty
            return new_funds, new_stocks
        else:
            print("Insufficient stock: {0} stocks owned, but selling {1}".format(stocks_owned,qty))
            return cash_balance, stocks_owned
    else:
        print("Ambigious transaction! Can't determine whether to buy ot sell. No action performed.")
        return cash_balance, stocks_owned


