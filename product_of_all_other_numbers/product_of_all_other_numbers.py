'''
Input: a List of integers
Returns: a List of integers
'''

from functools import reduce
def product_of_all_other_numbers(arr):
    # # Your code here
    sum = 1

    # NAIVE 
    # new_arr = arr
    # for i in arr:
    #     sum *= i
    # final = [sum//i for i in arr]
    # return final
    

    # NOT WORKING YET, LIKELY TOO SLOW ANYWAY
    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         print('j', arr[j])  
    #     # new_arr.pop(arr[i])
    #     # for j in range(len(new_arr)):
    #         # print(new_arr[i])
    #     sum = sum * arr[i]
    # # sum = sum/new_arr[i]
    # return sum/arr[i]

    # OPTIMIZED
    for i in arr:
        sum = sum * i 
    return [sum/i for i in arr]



    #fancy solution, which I don't understand yet
    # final = []

    # for i, el in enumerate(arr):
    #     final.append(reduce(lambda x, y: x*y, arr[:i] + arr[i+1:]))
    # return final
    

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [4, 2, 3, 1, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
