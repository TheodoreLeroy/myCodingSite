


def inputArraySize():
    """_summary_
        For user input array size
    Returns:
        int: array size
    """
    return int(input("Enter array size:"))
# end def


def inputArrayElement(arrSize):
    """_summary_
        For user input each index value
    Args:
        arrSize (int): size of array
        array (list): list to store value
    Returns:
        list: an array with user input value
    """
    array = []
    # loop to access each index of array and assign value to it
    for i in range(arrSize):
        array.append(int(input(f"Enter value for index {i}: ")))
    return array

def DisplayArray(array, msg):
    """_summary_
        A function to display the array
    Args:
        array (list): the unsorted or sorted array
        msg (_type_): messenger from server
    """
    print(msg)
    # loop to access each index of array and display it value
    for value in array:
        print(value, end=" ")
    print()
    pass

def SortArrayBubbleSort(unsortArr):
    length = len(unsortArr)
    # loop to reset the inner loop, each reset one highest value is sorted
    for j in range(length-1):
        # loop to access each value in the array
        for i in range(length-1):
            # compare current value with next value
            if unsortArr[i] > unsortArr[i+1]:
                unsortArr[i], unsortArr[i+1] = unsortArr[i+1], unsortArr[i]           
    return unsortArr

if __name__ == "__main__":
    # step 1: user input array size
    arrSize = inputArraySize()
    # step 2: user input array element by array size
    unsortArr = inputArrayElement(arrSize)
    # step 3: display unsort array
    DisplayArray(unsortArr, "Unsorted array: ")
    # step 4: sort array by bubble sort
    sortedArr = SortArrayBubbleSort(unsortArr)
    # step 5: display sorted array
    DisplayArray(sortedArr, "Sorted array: ")