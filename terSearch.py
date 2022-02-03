# time complexity O(log3 n)

def ternarySearch(arr, left, right, x):
    # base condition
    if right >= left:
        partitionSize = (right - left) // 3
        mid1 = left + partitionSize
        mid2 = right - partitionSize

        if arr[mid1] == x:
            return mid1

        if arr[mid2] == x:
            return mid2

        if x < arr[mid1]:
            return ternarySearch(arr, left, mid1 - 1, x)

        if x > arr[mid2]:
            return ternarySearch(arr, mid2 + 1, right, x)

        if x > arr[mid1] and x < arr[mid2]:
            return ternarySearch(arr, mid1 + 1, mid2 - 1, x)

    return -1
