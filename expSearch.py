# time complexity O(log i) ... i = position of the target
from binSearch import binarySearch


def exponentialSearch(arr, x):

    limit = 1
    while limit < len(arr) and arr[limit] < x:
        limit *= 2

    return binarySearch(arr, limit//2, min(limit, len(arr) - 1), x)
