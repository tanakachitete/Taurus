"""
NAME: ExchangeInfoGetter.py
AUTHOR: Tanaka Chitete
PURPOSE: Get exchange info from Binance API
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

"""
NAME: getExchangeInfoFromAPI
IMPORT(S): exchangeInfo (dict)
EXPORT(S): None
PURPOSE: Get exchange info from Binance API
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

def getExchangeInfoFromAPI(exchangeInfo):
    try:
        request = "https://api.binance.com/api/v3/exchangeInfo"
        exchangeInfo = JSON_IO.readFromUrl(request)
    except:
        print("Failed to make live request")