#example of linear run time algo O(n)
def linear_search(list, target):
    #returns index position of the target, else returns none
    for i in range(0, len(list)):
        #iterate over list 
        if list[i] ==target:
            #if index matches target value return index position
            return i 
    #if none match target value, return none
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
result = linear_search(numbers, 12)
verify(result)
#check for position of 6, position 5 in list
result = linear_search(numbers, 6)
verify(result)



"""
1:17:30 left off data structures and algos
"""