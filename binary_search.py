def binary_search(list, target):
    # first position in list
    first = 0
    #gets position of last element in list by determining length of list and subtracting 1
    last = len(list) - 1

    #keep executing while first is less than or equal to the last position
    while first <= last:
        #calculate midpoint of list
        #floor division operator rounds down to nearest whole number
        midpoint = (first + last)//2 

        #comparison tests
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first =  midpoint + 1
        else:
                last = midpoint - 1
                #if midpoint never equals target, the list never contained the target value return none
    return None

#function to verify that algo works correctly
def verify(index):
    #if index is found to match target return this
    if index is not None:
        print("Target found at index: ", index)
    else:
        #if target is not found in list return this
        print("Target not found in list")

#sample array
numbers = [1,2,3,4,5,6,7,8,9,10]

#check for position of 12, not in list
result = binary_search(numbers, 12)
verify(result)
#check for position of 6, position 5 in list
result = binary_search(numbers, 6)
verify(result)


