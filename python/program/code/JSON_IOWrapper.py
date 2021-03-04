"""
NAME: JSON_IOWrapper.py
AUTHOR: Tanaka Chitete
PURPOSE: Implement wrappers for submodules in JSON_IO.py
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

import UserInterface

"""
NAME: loadFromFile
IMPORT(S): dictionary (dict)
EXPORT(S): None
PURPOSE: Load JSON object from file to dictionary
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

def loadFromFile(dictionary):
    try:
        prompt = "Filename: "
        filename = UserInterface.getStr(prompt)
        print() # Formatting purposes

        dictionary = JSON_IO.readFromFile(filename)
    except:
        print("Failed to load from file")


"""
NAME: saveToFile
IMPORT(S): dictionary (dict)
EXPORT(S): None
PURPOSE: Save dictionary to file
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

def saveToFile(marketInfo):
    if marketInfo is None:
        print("Cannot save to file before making live request or loading from file")
    else:
        try:
            prompt = "Filename (without extension): "
            filename = UserInterface.getStr(prompt)
            filename += ".json"
            print() # Formatting purposes

            JSON_IO.writeToFile(marketInfo, filename)

            print(f"File saved as: {filename} in current directory")
        except:
            print("Failed to save to file")