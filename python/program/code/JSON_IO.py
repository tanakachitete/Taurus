"""
NAME: Taurus
AUTHOR: Tanaka Chitete
PURPOSE: Read and write JSON objects obtained from either APIs or files
CREATION: 03/03/2021
LAST MODIFICATION: 03/03/2021
"""

import json
import requests

"""
NAME: readFromUrl
IMPORT(S): Url (str)
EXPORT(S): dictionary (dict)
PURPOSE: Read and parse JSON object obtained from API
CREATION: 03/03/2021
LAST MODIFICATION:
"""

def readFromUrl(Url):
    # Contacts API
    try:
        response = requests.get(Url)
        response.raise_for_status()
    except requests.RequestException:
        raise Exception

    # Parses response
    try:
        dictionary = response.json()
        return dictionary
    except (KeyError, TypeError, ValueError):
        raise Exception


"""
NAME: readFromFile
IMPORT(S): filename (str)
EXPORT(S): dictionary (dict)
PURPOSE: Read and parse JSON object obtained from file
CREATION: 03/03/2021
LAST MODIFICATION: 03/03/2021
"""

def readFromFile(filename):
    try:
        with open(filename, "r") as f:
            dictionary = json.load()
        return dictionary
    except (OSError, KeyError, TypeError, ValueError):
        raise Exception


"""
NAME: writeToFile
IMPORT(S): filename (str), dictionary (dict)
EXPORT(S): None
PURPOSE: Write JSON object (as dict) to file
CREATION: 03/03/2021
LAST MODIFICATION: 03/03/2021
"""

def writeToFile(filename, dictionary):
    try:
        with open(filename, "w") as f:
            json.dump(dictionary, f)
    except(OSError, KeyError, TypeError, ValueError):
        raise Exception