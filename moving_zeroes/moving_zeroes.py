'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    #ints not equal to 0 add to an array and return the length
    #move non zeros to left in order they appear in array
    #create for non zeros, append zeroes at the end 
    #use for loop to add non zeroes 
    #outside the for loop add zeroes
    #add zeroes to a different list
    #add the zeroes list to non zeroes list
    real =[]
    zeroes = []
    for x in arr:
        if x != 0:
            real.append(x)
        if x == 0:
            zeroes.append(x)
    combined = real + zeroes
    return combined

 

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")