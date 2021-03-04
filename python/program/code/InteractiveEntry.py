"""
NAME: InteractiveEntry
AUTHOR: Tanaka Chitete
PURPOSE: Implement entry point for Interactive mode operations
CREATION: 03/03/2021
LAST MODIFICATION: 03/03/2021
"""

import InteractiveAnalyser
import InteractiveAndReportAnalyser
import Set
import UserInterface

"""
NAME: menu
IMPORT(S): None
EXPORT(S): None
PURPOSE: Print menu and prepare to launch user-specified operation
CREATION: 03/03/2021
LAST MODIFICATION: 03/03/2021
"""

def menu():
    excludedAssets = Set()
    userInput = None
    while True:
        print("Taurus (Interactive Mode)\n\n" + \
            "1. Get and Display Market Information of Given Trade Pair\n" + \
            "2. Get and Display Recent Trades (sorted by price, quantity and quote)\n" + \
            "3. Get and Display All Trade Paths Between Two Given Assets\n" + \
            "4. Get and Display All Trade Pairs Involving Given Asset\n" + \
            "5. Get and Display Asset Filtered Trade Pairs\n" + \
            "6. Configure Asset Filter\n" + \
            "0. Quit\n"
        )   
        prompt = "Selection: "
        userInput = UserInterface.getInt(0, 6, prompt)
        print() # Formatting purposes

        if userInput == 0:
            break
        else:
            launch(userInput, excludedAssets)


"""
NAME: launch
IMPORT(S): userInput (int), excludedAssets (Set)
EXPORT(S): None
PURPOSE: Launch user-specified operation
CREATION: 03/03/2021
LAST MODIFICATION: 03/03/2021
"""

def launch(userInput, excludedAssets):
    if userInput == 1:
        MarketInfo.subMenu()
    elif userInput == 2:
        RecentTrades.subMenu()
    elif userInput == 3:
        TradePaths.subMenu()
    elif userInput == 4:
        TradePairs.subMenu()
    elif userInput == 5:
        FilteredTradePairs.subMenu()
    elif userInput == 6:
        AssetFilter.subMenu()