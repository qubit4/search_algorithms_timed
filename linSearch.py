# time complexity O(n)

def linearSearch(arr, x):

    for i in range(0, len(arr)):
        if(arr[i] == x):
            return i

    return -1
