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
            "1. Get and Display Market Information of Given Trade Pair\n" + \
            "2. Get and Display Recent Trades (sorted by price, quantity and quote)\n" + \
            "3. Get and Display All Trade Paths Between Two Given Assets\n" + \
            "4. Get and Display All Trade Pairs Involving Given Asset\n" + \
            "5. Get and Display Asset Filtered Trade Pairs\n" + \
            "6. Configure Asset Filter\n" + \
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
    if userInput == 1:
        InteractiveAnalyser.getAndDisplayMarketInformationOfGivenTradePair()
    elif userInput == 2:
        InteractiveAnalyser.getAndDisplayRecentTrades()
    elif userInput == 3:
        InteractiveAnalyser.getAndDisplayAllTradePathsBetweenTwoGivenAssets()
    elif userInput == 4:
        InteractiveAnalyser.getAndDisplayAllTradePairsInvolvingGivenAsset()
    elif userInput == 5:
        InteractiveAnalyser.getAndDisplayAssetFilteredTradePairs()
    elif userInput == 6:
        InteractiveAndReportAnalyser.configureAssetFilter()