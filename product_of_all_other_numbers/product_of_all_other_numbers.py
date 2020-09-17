'''
Input: a List of integers
Returns: a List of integers
'''
#take product of each number in the list to the other number EXCEPT for the current index 
# add all products to a list
# return the list of all products
# find product using math 

def product_of_all_other_numbers(arr):
    import math
    products = []
    if len(arr) == 2: 
        arr[0], arr[1] = arr[1], arr[0]
    if len(arr) > 2:
        for i in range(len(arr)):
            focus = arr[0:i] + arr[i+1:]
            each_product = (focus)
            products.append(each_product)
        return products



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    #arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
