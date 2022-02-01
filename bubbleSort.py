def bubbleSort(array):

    # loop to access each element
    for i in range(len(array)):

        swapped = False

        # loop to compare each element
        for j in range(0, len(array) - i - 1):

            if array[j] > array[j+1]:
                # swapping right and left element if left is greater than right
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                swapped = True

        # if the array is already sorted, the function ends
        if not swapped:
            break
