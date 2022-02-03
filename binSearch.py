# works only on sorted lists
# time complexity O(log n)
# space complexity O(log n)

# recursive implementation
def binarySearch(arr, left, right, x):
    # base condition
    if right >= left:

        mid = (left + right) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binarySearch(arr, left, mid - 1, x)

        if arr[mid] < x:
            return binarySearch(arr, mid + 1, right, x)

    return -1


# iterative implementation
def binarySearch_it(arr, left, right, x):
    left = 0
    right = len(arr) - 1

    while right >= left:
        mid = left + right // 2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            right = mid - 1

        else:
            left = mid + 1

        return -1
