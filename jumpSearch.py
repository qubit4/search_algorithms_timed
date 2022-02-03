# time complexity O(√n)
import math


def jumpSearch(arr, x):

    # size of the jump block is most efficient as square root of len(arr)
    blockSize = int(math.sqrt(len(arr)))
    start = 0
    next = blockSize

    # jumping through the array until finding the block containing x
    while arr[next - 1] < x and start < len(arr):
        start = next
        next += blockSize

        # if the last block has fewer numbers
        if next > len(arr):
            next = len(arr)

    # starting linear search from left to right in the correct block
    for i in range(start, next):
        if arr[i] == x:
            return i

    return -1
