import math


def jumpSearch(arr, n, x):

    # length of the jump block is most efficient as square root of len(arr)
    step = math.sqrt(len(arr))
    prev = 0

    # jumping through the array until finding the block containing x
    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)

        if prev >= n:
            return -1

    # starting linear search from left to right in the correct block
    for i in range(int(prev), int(step)):
        if arr[i] == x:
            return i

    return -1
