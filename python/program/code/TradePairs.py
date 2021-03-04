"""
NAME: TradePairs.py
AUTHOR: Tanaka Chitete
PURPOSE: Get and print all trade pairs involving crypto-currency
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

import JSON_IOWrapper
import Quicksort
import TradePairsAndTradePathsHelper
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
    exchangeInfo = None
    while True:
        print("Get and Display All Trade Pairs Involving Asset\n\n" + \
            "1. Display\n" + \
            "2. Make Live Request\n" + \
            "3. Load from File\n" + \
            "4. Save to File\n" + \
            "0. Exit\n"
        )
        prompt = "Selection: "
        selection = UserInterface.getInt(0, 4, prompt)
        
        print() # Formatting purposes

        if selection == 1:
            printAllTradePairs(exchangeInfo)
        elif selection == 2:
            TradePairsAndTradePathsHelper.getExchangeInfoFromAPI(exchangeInfo)
        elif selection == 3:
            JSON_IOWrapper.loadFromFile(exchangeInfo)
        elif selection == 4:
            JSON_IOWrapper.saveToFile(exchangeInfo)
        else:
            break


"""
NAME: printAllTradePairs
IMPORT(S): exchangeInfo (dict)
EXPORT(S): None
PURPOSE: Print all currently-trading trade pairs
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

def printAllTradePairs(exchangeInfo):
    if exchangeInfo is None:
        print("Cannot display before making live request or loading from file")
    else:
        tradePairs = Quicksort.quicksort(exchangeInfo["symbols"])

        prompt = "Crypto-currency (case-insensitive): "
        crypto = UserInterface.getStr(prompt)
        crypto = crypto.upper()

        print() # Formatting purposes

        for pair in tradePairs:
            # Ensures only active trade pairs are considered
            if pair["status"] == "TRADING": 
                # Prints trade pair if user-specified crypto-currency is either base or quote
                if crypto == pair["baseAsset"]:
                    print(pair["symbol"])
                elif crypto == pair["quoteAsset"]:
                    print(pair["symbol"])