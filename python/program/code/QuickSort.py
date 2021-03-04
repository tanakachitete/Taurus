"""
NAME: QuickSort.py
AUTHOR: Tanaka Chitete
PURPOSE: Sort recentTradesList by keyStat value using self-implemented Quicksort
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

"""
NAME: quicksort
IMPORT(S): recentTradesList (list), low (int), high (int), keyStat (str)
EXPORT(S): None
PURPOSE: Implements frontend of self-implemented Quicksort
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

def quicksort(recentTradesList, low, high, keyStat):
    if low < high:
        # recentTradesList[partitionIndex] is now at correct place
        partitionIndex = partition(recentTradesList, low, high, keyStat)

        # Sort to the left of recentTradesList[partitionIndex]
        quicksort(recentTradesList, low, partitionIndex - 1, keyStat)
        # Sort to the right of recentTradesList[partitionIndex]
        quicksort(recentTradesList, partitionIndex + 1, high, keyStat)


"""
NAME: partition
IMPORT(S): recentTradesList (list), low (int), high (int), keyStat (str)
EXPORT(S): None
PURPOSE: Take last trade (dict) of recentTradesList and use its keyStat value it as pivot, place 
    last trade at its correct position in sorted array and place all trades with keyStat value 
    less than last trade to the left of last trade and all trades with keyStat value greater 
    than last trade to the right of last trade
CREATION: 04/03/2021
LAST MODIFICATION: 04/03/2021
"""

def partition(recentTradesList, low, high, keyStat):
    # Element to be placed at correct position
    pivot = recentTradesList[high]

    # Index of smaller element and indicates the correct position of pivot found so far
    i = (low - 1)

    for j in range(low, high):
        if recentTradesList[j][keyStat] < pivot[keyStat]:
            i += 1
            # Swaps recentTradesList[i] and recentTradesList[j]
            temp = recentTradesList[i]
            recentTradesList[i] = recentTradesList[j]
            recentTradesList[j] = temp
    # Swaps recentTradesList[i + 1] and recentTradesList[high]
    temp = recentTradesList[i + 1]
    recentTradesList[i + 1] = recentTradesList[high]
    recentTradesList[high] = temp

    return i + 1