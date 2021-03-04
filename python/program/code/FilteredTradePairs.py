"""
NAME: FilteredTradePairs.py
AUTHOR: Tanaka Chitete
PURPOSE: Get and print crypto-filtered trade pairs
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

import ExchangeInfoGetter
import JSON_IOWrapper
import Quicksort
import UserInterface

"""
NAME: subMenu
IMPORT(S): assetFilter (Set)
EXPORT(S): None
PURPOSE: Print sub-menu and prepare to launch user-specified operation
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

def subMenu(assetFilter):
    exchangeInfo = None
    while True:
        print("Get and Display Crypto-Filtered Trade Pairs\n\n" + \
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
            printFilteredTradePairs(exchangeInfo, assetFilter)
        elif selection == 2:
            ExchangeInfoGetter.getExchangeInfoFromAPI(exchangeInfo)
        elif selection == 3:
            JSON_IOWrapper.loadFromFile(exchangeInfo)
        elif selection == 4:
            JSON_IOWrapper.saveToFile(exchangeInfo)


"""
NAME: printFilteredTradePairs
IMPORT(S): exchangeInfo (dict), assetFilter (Set)
EXPORT(S): None
PURPOSE: Print crypto-filtered trade pairs
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

def printFilteredTradePairs(exchangeInfo, assetFilter):
    if exchangeInfo is None:
        print("Cannot display before making live request or loading from file")
    else:
        tradePairs = Quicksort.quicksort(exchangeInfo["symbols"])

        for pair in tradePairs:
            # Ensures only active trade pairs are considered
            if pair["status"] == "TRADING":
                # Prints pair if neither base nor quote was added to asset filter
                if not assetFilter.has(pair["baseAsset"]) or not assetFilter.has(pair["quoteAsset"]):
                    print(pair["symbol"])
        
        print() # Formatting purposes

        print(f"Excluded Assets: {assetFilter}\n")