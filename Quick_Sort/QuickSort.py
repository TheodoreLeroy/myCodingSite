import random

def inputSizeOfArray():
    """Function for user to input size of array

    Returns:
        Integer: size of the array
    """
    return int(input("Enter number of array:"))
# end def

def generateRandomArray(size):
    array = []
    # loop to access each index of the array
    for i in range(size):
        array.append(random.randint(0, size))
    return
# end def

def displayArray(array, msg):
    """
    Purpose: Function to display the array sequently
    """
    print(msg)
    # loop to access each value from array and display its
    for value in array:
        print(value, "", end=" ")
    print()
    return
# end def

def sortArrayByQuickSort(unsortedArray):
    """
    Purpose: Function to sort array by quick sort algorithm using recursive
    """
    # i move from first one (increase), j move from last one (decrease)
    # base case: i > j (stop)
    # Find a pivot
    """Beginning of partition: 
    - move i until find value equal or greater than pivot value
    - move j until find value equal or lower than pivot value
    - compare value of i and value of j if i <= j then swap
    """
    def partition(unsortedArray):
        # Find a pivot
        pivot = int(len(unsortedArray)/2)
        # Loop to access each index of array, increase first and last after each number is sorted
        for i in range(len(unsortedArray)):
            quickSort(unsortedArray, i, len(unsortedArray)-i-1, pivot)


    def quickSort(array, first, last, pivot):
        # Find first >= pivot and last <= pivot
        # Compare first and last (base case)
        if first > last:
            return
        print(f"Current first: {array[first]} of index [{first}]")
        print(f"Current last: {array[last]} of index [{last}]")
        displayArray(array, "The array:")
        print()
        # Compare value of first and pivot
        if array[first] < array[pivot]:
            quickSort(array, first+1, last, pivot)
        # Compare value of last and pivot
        elif array[last] > array[pivot]:
            quickSort(array, first, last-1, pivot)
        else:
            print(f"{array[first]} swap with {array[last]}, the pivot is {array[pivot]}")
            print("---------------------")
            print()
            swapValue(array, first, last)
        print()



    def swapValue(array, index1, index2):
        array[index1], array[index2] = array[index2], array[index1]

    partition(unsortedArray)
    return unsortedArray
# end def

if __name__  == "__main__":
    # step 1: user input size of array
    arraySize = inputSizeOfArray()
    # step 2: generate random value by array size
    unsortedArray = generateRandomArray(arraySize)
    unsortedArray = [1, 12, 5, 26, 7, 14, 3, 7, 2]
    # step 3: display unsorted array
    displayArray(unsortedArray, "Unsorted array: ")
    # step 4: sort array by quick sort
    sortedArray = sortArrayByQuickSort(unsortedArray)
    # step 5: display sorted array
    displayArray(sortedArray, "Sorted array: ")
