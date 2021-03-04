"""
NAME: RecentTrades.py
AUTHOR: Tanaka Chitete
PURPOSE: Get and print user-specified number of recent trades (sorted by price, quantity and quote)
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

import datetime
import JSON_IOWrapper
import RecentTradesHelper
import UserInterface

"""
NAME: subMenu
IMPORT(S): None
EXPORT(S): None
PURPOSE: Print sub-menu and prepare to launch user-specified operation
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

def subMenu():
    recentTrades = None
    while True:
        print("Get and Display Recent Trades (sorted by price, quantity and quote)\n\n" + \
            "1. Display\n" + \
            "2. Make Live Request\n" + \
            "3. Load from File\n" + \
            "4. Save to File\n" + \
            "0. Exit\n"
        )
        prompt = "Selection: "
        selection = UserInterface.getInt()
        print() # Formatting purposes

        if selection == 1:
            printRecentTrades(recentTrades)
        elif selection == 2:
            getRecentTradesFromAPI(recentTrades)
        elif selection == 3:
            JSON_IOWrapper.loadFromFile(recentTrades)
        elif selection == 4:
            JSON_IOWrapper.saveToFile(recentTrades)
        else:
            break


"""
NAME: printRecentTrades
IMPORT(S): recentTrades (dict)
EXPORT(S): None
PURPOSE: Print recent trades sorted by Price, Quantity and Quote
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

def printRecentTrades(recentTrades):
    if recentTrades is None:
        print("Cannot display before making live request or loading from file")
    else:
        # Dictionaries are un-sortable so conversion to list is required
        recentTradesList = [trade for trade in recentTrades]
        
        keyStats = ["price", "qty", "quoteQty"]
        printStats = ["Price", "Quantity", "Quote"]
        for (keyStatistic, printStatistic) in zip(keyStats, printStats):
            RecentTradesHelper.quicksort(recentTradesList, "price")

            print(f"Top {len(recentTradesList)} Trades Sorted by {printStatistic}")

            # Iterates in reverse to print recent trades in descending order
            for i in range(len(recentTradesList) - 1, -1, -1):
                iZeroIndex = i
                iOneIndex = i + 1
                currTrade = recentTradesList[iZeroIndex]
                print(f"{iZeroIndex}")
                print(f"{currTrade[keyStatistic]}") # TODO - Add formatting
                print(f"{datetime.datetime(currTrade['time'])}\n")


"""
NAME: getRecentTradesFromAPI
IMPORT(S): marketInfo (dict)
EXPORT(S): None
PURPOSE: Get market info from Binance API
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

def getRecentTradesFromAPI():
    try:
        prompt = "Base crypto-currency (case-insensitive): "
        base = UserInterface.getStr(prompt)
        prompt = "Quote crypto-currency (case-insensitive): "
        quote = UserInterface.getStr(prompt)
        print() # Formatting purposes

        tradePair = base + quote
        tradePair = tradePair.upper()

        prompt = "Number of trades to view: "
        numTradesToView = UserInterface.userInput(1, 100, prompt)
        print() # Formatting purposes

        request = f"https://api.binance.com/api/v3/trades?symbol={tradePair}&limit={numTradesToView}"
        recentTrades = JSON_IO.readFromUrl(request)
    except:
        print("Failed to make live request")