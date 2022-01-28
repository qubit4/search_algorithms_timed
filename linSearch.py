def linearSearch(arr, n, x):

    for i in range(0, n):
        if(arr[i] == x):
            return i

    return -1


print("This script creates an array of numbers from user input and searches for the target number with linear search algorithm.")

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

        # searching for target with binary search algorithm
        result = linearSearch(arr, len(arr), target)
        print("Target element is present at index", result)

    except ValueError:
        print("Not a valid input")
