def binarySearch(arr, l, r, x):

    if r >= l:
        mid = l + (r-l) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        else:
            return binarySearch(arr, mid+1, r, x)

    else:
        return -1


print("This script creates an array of numbers from user input and searches for the target number with binary search algorithm.")

# main loop
while True:

    try:
        # creating an array and the target from user input
        arr = []
        count = int(input("Number of elements: "))

        for i in range(0, count):
            elem = int(input("Enter the element: "))
            arr.append(elem)
        print('The present array is:', arr)

        target = int(
            input("Enter the element you want to search for in the present array: "))

        # searching for the target with binary search algorithm
        result = binarySearch(arr, 0, len(arr)-1, target)
        print("Target element is present at index", result)

    except ValueError:
        print("Not a valid input")
