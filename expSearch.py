from binSearch import binarySearch


def exponentialSearch(arr, n, x):
    if arr[0] == x:
        return 0

    i = 1
    while i < n and arr[i] <= x:
        i = i * 2

    return binarySearch(arr, i//2, min(i, n - 1), x)
