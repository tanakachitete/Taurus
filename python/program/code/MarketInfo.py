"""
NAME: MarketInfo.py
AUTHOR: Tanaka Chitete
PURPOSE: Implement core logic for getting and displaying market info of given trade pair
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

import datetime
import JSON_IOWrapper
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
    marketInfo = None
    while True:
        print("Get and Display Market Information of Given Trade Pair\n\n" + \
            "1. Display\n" + \
            "2. Make Live Request\n" + \
            "3. Load from File\n" + \
            "4. Save to File\n" + \
            "0. Exit\n"
        )
        prompt = "Input: "
        selection = UserInterface.getInt(0, 4, prompt)
        print() # Formatting purposes

        if selection == 1:
            printMarketInfo(marketInfo)
        elif selection == 2:
            getMarketInfoFromAPI(marketInfo)
        elif selection == 3:
            JSON_IOWrapper.loadFromFile(marketInfo)
        elif selection == 4:
            JSON_IOWrapper.saveToFile(marketInfo)
        else:
            break


"""
NAME: printMarketInfo
IMPORT(S): marketInfo (dict)
EXPORT(S): None
PURPOSE: Print market info
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

def printMarketInfo(marketInfo):
    if marketInfo is None:
        print("Cannot display before making live request or loading from a file")
    else:
        print(f"{marketInfo['symbol']} Market Information\n")

        print(f"Open Time (system time):  {datetime.datetime(marketInfo['openTime'])}")
        print(f"Close Time (system time): {datetime.datetime(marketInfo['closeTime'])}\n")

        print(f"Latest Price (USD):       {marketInfo['lastPrice']}")
        print(f"Price Change (USD):       {marketInfo['priceChange']}")
        print(f"Price Change (%):         {marketInfo['priceChangePercent']}")        


"""
NAME: getMarketInfoFromAPI
IMPORT(S): marketInfo (dict)
EXPORT(S): None
PURPOSE: Get market info from Binance API
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

def getMarketInfoFromAPI(marketInfo):
    try:
        prompt = "Base crypto-currency (case-insensitive): "
        base = UserInterface.getStr(prompt)
        prompt = "Quote crypto-currency (case-insensitive): "
        quote = UserInterface.getStr(prompt)
        print() # Formatting purposes

        tradePair = base + quote
        tradePair = tradePair.upper()

        request = f"https://api.binance.com/api/v3/ticker/24hr?symbol={tradePair}"
        marketInfo = JSON_IO.readFromUrl(request)
    except:
        print("Failed to make live request")