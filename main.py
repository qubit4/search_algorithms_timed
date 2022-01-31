from linSearch import linearSearch
from jumpSearch import jumpSearch
from binSearch import binarySearch
from expSearch import exponentialSearch
from fibonacci_cache import fibonacci_of
from timeit import default_timer
from datetime import timedelta

print("This program explores different search algorithms for numerical arrays.")

while True:

    try:
        # creating an array of numbers
        array_option = int(input(
            "\n1. I want to manually create an array of numbers. 2. I want to use Fibonacci sequence. 3. Quit  || Press 1 or 2 or 3: "))

        if array_option == 1:

            arr = []
            count = int(input("Number of elements in the array? "))

            for i in range(0, count):
                elem = int(input("Enter the element: "))
                arr.append(elem)
            print('The present array is:', arr)

        if array_option == 2:

            count = int(
                input("Number of elements in the Fibonacci sequence? "))
            arr = [fibonacci_of(n) for n in range(count)]
            print('The present array is:', arr)

        if array_option == 3:
            quit()

        # selecting target number
        target = int(
            input("Enter the element you want to search for in the present array: "))

        # search with 4 search algorithms, timing the search and printing results
        print("\nRESULTS \n")

        start1 = default_timer()
        result1 = linearSearch(arr, len(arr), target)
        end1 = default_timer()
        time_linear = timedelta(seconds=end1-start1)

        print("Linear Search")
        print("Target element is present at index", result1)
        print("Search executed in {} seconds".format(time_linear))

        start2 = default_timer()
        result2 = jumpSearch(arr, len(arr), target)
        end2 = default_timer()
        time_jump = timedelta(seconds=end2-start2)

        print("Jump Search")
        print("Target element is present at index", result2)
        print("Search executed in {} seconds".format(time_jump))

        start3 = default_timer()
        result3 = binarySearch(arr, 0, len(arr)-1, target)
        end3 = default_timer()
        time_binary = timedelta(seconds=end3-start3)

        print("Binary Search")
        print("Target element is present at index", result3)
        print("Search executed in {} seconds".format(time_jump))

        start4 = default_timer()
        result4 = exponentialSearch(arr, len(arr), target)
        end4 = default_timer()
        time_exponential = timedelta(seconds=end4-start4)

        print("Exponential Search")
        print("Target element is present at index", result4)
        print("Search executed in {} seconds".format(time_exponential))

    except ValueError:
        print("Not a valid input")
