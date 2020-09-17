'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
#return the repeated integer
def single_number(arr):
    #check each index if it matches the next
    #check each int if it appears again
    #may create a copy of the list to compare
    
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            print(arr[i])
            print(arr[j])
            if arr[i] == arr[j]:
                i +=2
                j +=2
            else:
                return arr[i]





    #make a dictionary


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")