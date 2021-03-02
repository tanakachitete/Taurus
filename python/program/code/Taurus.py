"""
NAME: Taurus
AUTHOR: Tanaka Chitete
PURPOSE: Implement entry point for Taurus crypto-currency data analysis suite
CREATION: 03/03/2021
LAST MODIFICATION: 03/03/2021
"""

import sys

def main():
    INTERACTIVE_ARGC = 2
    REPORT_ARGC = 4

    INTERACTIVE_MODE = "-i"
    REPORT_MODE = "-r"

    # User provided incorrect number of CLAs for either mode
    if len(sys.argv) != INTERACTIVE_ARGC and len(sys.argv) != REPORT_ARGC:
        print("Usage (Interactive): python Taurus.py -i")
        print("or")
        print("Usage (Report): python Taurus.py -r <asset filename> <trade filename>")
    else:
        mode = sys.argv[1]
        # User wants to run program in Interactive mode
        if mode == INTERACTIVE_MODE:
            if len(sys.argv) != INTERACTIVE_ARGC:
                print("Usage (Interactive): python Taurus -i")
            else:
                print() # Formatting
                InteractiveEntry.entry()
        # User wants to run program in Report mode
        elif mode == REPORT_MODE:
            assetFilename = sys.argv[2]
            tradeFilename = sys.argv[3]
            if len(sys.argv[1]) != REPORT_ARGC:
                print("Usage (Report): python Taurus.py -r <asset filename> <trade filename>")
            else:
                print() # Formatting
                ReportEntry.entry(assetFilename, tradeFilename)
        # User hasn't specified that they want to run program in either Interactive or Report
        else:
            print("Usage (Interactive): python Taurus.py -i")
            print("or")
            print("Usage (Report): python Taurus.py -r <asset filename> <trade filename>")            


main()