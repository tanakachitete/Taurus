"""
NAME: InteractiveEntry
AUTHOR: Tanaka Chitete
PURPOSE: Implement entry point for Interactive mode
CREATION: 03/03/2021
LAST MODIFICATION: 02/03/2021
"""

import InteractiveAnalyser
import InteractiveAndReportAnalyser
import Set
import UserInterface

"""
NAME: entry
IMPORT(S): None
EXPORT(S): None
PURPOSE: Print Interactive mode menu, retrieve user input and prepare to launch specified operation
CREATION: 03/03/2021
LAST MODIFICATION: 03/03/2021
"""

def entry():
    QUIT = 0
    OPTION_6 = 6

    excludedAssets = Set()
    userInput = None
    while True:
        print("Interactive Menu\n\n" + \
            "1. Asset Details\n" + \
            "2. Trade Details\n" + \
            "3. Trade Paths\n" + \
            "4. Asset Filter\n" + \
            "5. Asset Overview\n" + \
            "6. Trade Overview\n" + \
            "0. Quit\n"
        )   
        prompt = "Input: "
        userInput = UserInterface.getInt(QUIT, OPTION_6, prompt)
        print() # Formatting purposes

        if userInput == QUIT:
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
    ASSET_DETAILS = 1
    TRADE_DETAILS = 2
    TRADE_PATHS = 3
    ASSET_FILTER = 4
    ASSET_OVERVIEW = 5
    # TRADE_OVERVIEW = 6, Unnecessary as userInput will be between 1 and 6 inclusive

    if userInput == ASSET_DETAILS:
        InteractiveAnalyser.getAssetTradePairs()
    elif userInput == TRADE_DETAILS:
        InteractiveAnalyser.getPriceChangeInfo()
    elif userInput == TRADE_PATHS:
        InteractiveAnalyser.getAssetGraph()
    elif userInput == ASSET_FILTER:
        InteractiveAndReportAnalyser.changeExcludedAssets()
    elif userInput == ASSET_OVERVIEW:
        InteractiveAnalyser.getAllTradePairs()
    else:
        InteractiveAnalyser.getRecentTrades()