#recursive search works by calling itself to continue working until it has an answer, it then works backwards giving the answer to every function that called it until the "original caller" has an answer

def recursive_binary_search(list, target):
    #if length of list is 0 return False stop search
    if len(list) == 0:
        return False
    else: 
        #calculate value of midpoint
        midpoint = (len(list))//2
        #is value at midpoint equal to target
        if list[midpoint] == target:
            return True
        else:
            #is value at the midpoint less than the target
            if list[midpoint] < target:
                #call function again with a sub list of first list starting at midpoint + 1 to the end
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8]

result = recursive_binary_search(numbers, 12)
verify(result)
result = recursive_binary_search(numbers, 6)
verify(result)

