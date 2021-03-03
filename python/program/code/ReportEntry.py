"""
NAME: ReportEntry
AUTHOR: Tanaka Chitete
PURPOSE: Implement entry point for Report mode operations
CREATION: 03/03/2021
LAST MODIFICATION: 03/03/2021
"""

import InteractiveAndReportAnalyser
import InteractiveAndReportPrinter
import InteractiveAndReportSorter
import JSON_IO
import Set
import UserInterface

"""
NAME: entry
IMPORT(S): assetFilename (str), tradeFilename (str)
EXPORT(S): None
PURPOSE: Read asset and trade files; retrieve user input and prepare to launch specified operation
CREATION: 03/03/2021
LAST MODIFICATION: 03/03/2021
"""

def entry(assetFilename, tradeFilename):
    QUIT = 0
    OPTION_3 = 3

    exchangeInfo = None
    try:
        exchangeInfo = JSON_IO.readFromFile(assetFilename)
    except:
        print(f"Failed to load {assetFilename}")
    
    recentTrades = None
    try:
        exchangeInfo = JSON_IO.readFromFile(tradeFilename)
    except:
        print(f"Failed to load {tradeFilename}")
    
    if exchangeInfo and recentTrades:
        assetFilter = Set()
        userInput = None
        while True:
            print("Report Menu\n\n" + \
                "1. Display Recent Trades (sorted by price, quantity and quote)\n" + \
                "2. Display Asset Filtered Trade Pairs\n" + \
                "3. Configure Asset Filter\n" + \
                "0. Quit\n"
            )
            prompt = "Input: "
            userInput = UserInterface.getInt(QUIT, OPTION_3, prompt)
            print() # Formatting purposes

            if userInput == QUIT:
                break
            else:
                launch(userInput, assetFilter)
    else:
        print("Cannot execute operations with invalid/non-existent asset and/or trade file")


"""
NAME: launch
IMPORT(S): userInput (int), assetFilter (Set), exchangeInfo (dict), recentTrades (dict)
EXPORT(S): None
PURPOSE: Launch user-specified operation
CREATION: 03/03/2021
LAST MODIFICATION: 03/03/2021
"""

def launch(userInput, assetFilter, exchangeInfo, recentTrades):
    if userInput == 1:
        InteractiveAndReportSorter.sortRecentTradesByPrice(recentTrades)
        InteractiveAndReportPrinter.printRecentTradesSortedByPrice(recentTrades)

        InteractiveAndReportSorter.sortRecentTradesByQty(recentTrades)
        InteractiveAndReportPrinter.printRecentTradesSortedByQty(recentTrades)

        InteractiveAndReportSorter.sortRecentTradesByQuote(recentTrades)
        InteractiveAndReportPrinter.printRecentTradesSortedByQuote(recentTrades)
    elif userInput == 2:
        InteractiveAndReportAnalyser.displayAssetFilteredTradePairs(exchangeInfo, assetFilter)
    elif userInput == 3:
        InteractiveAndReportAnalyser.configureAssetFilter(assetFilter)
