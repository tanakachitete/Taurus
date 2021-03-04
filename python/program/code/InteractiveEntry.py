"""
NAME: InteractiveEntry
AUTHOR: Tanaka Chitete
PURPOSE: Act as entry point for Taurus (Interactive Mode)
CREATION: 03/03/2021
LAST MODIFICATION: 04/03/2021
"""

import RecentTrades
import MarketInfo
import Set
import TradePairs
import TradePaths
import UserInterface

"""
NAME: menu
IMPORT(S): None
EXPORT(S): None
PURPOSE: Print menu and prepare to launch user-specified operation
CREATION: 03/03/2021
LAST MODIFICATION: 04/03/2021
"""

def menu():
    assetFilter = Set()
    userInput = None
    while True:
        print("Taurus (Interactive Mode)\n\n" + \
            "1. Get and Display Market Information of Trade Pair\n" + \
            "2. Get and Display Recent Trades (sorted by price, quantity and quote)\n" + \
            "3. Get and Display All Trade Paths Between Two Crypto-currencies\n" + \
            "4. Get and Display All Trade Pairs Involving Crypto-currency\n" + \
            "5. Get and Display Crypto-Filtered Trade Pairs\n" + \
            "6. Configure Crypto Filter\n" + \
            "0. Quit\n"
        )   
        prompt = "Selection: "
        userInput = UserInterface.getInt(0, 6, prompt)
        print() # Formatting purposes

        if userInput == 0:
            break
        else:
            launch(userInput, assetFilter)


"""
NAME: launch
IMPORT(S): userInput (int), assetFilter (Set)
EXPORT(S): None
PURPOSE: Launch user-specified operation
CREATION: 03/03/2021
LAST MODIFICATION: 04/03/2021
"""

def launch(userInput, assetFilter):
    if userInput == 1:
        MarketInfo.subMenu()
    elif userInput == 2:
        RecentTrades.subMenu()
    elif userInput == 3:
        TradePaths.subMenu()
    elif userInput == 4:
        TradePairs.subMenu()
    elif userInput == 5:
        FilteredTradePairs.subMenu(assetFilter)
    elif userInput == 6:
        AssetFilter.subMenu(assetFilter)