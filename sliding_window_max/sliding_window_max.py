'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
#what if k is larger than len(nums)? Go with a reasonable interpretation, then follow through 
#can use a queue
# 1. max queue length == k 
# 2. the front queue element is always going to be the max of all the queue 

def sliding_window_max(nums, k):
    # Your code here

    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
