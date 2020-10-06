'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
import time

# input: arr of numbers where thre is one number that is not a duplicate; 
# every other number has a dupe
# def single_number(arr):
#     # Your code here
#     # O(n**2)

#     for num in arr: # O(n)
#         if arr.count(num) == 1: # O(n)
#             return num


def single_number(arr):
    # sets are closely related cousin to dictionaries
    # do not associate values with keys
    # useful when you need the uniqueness properties of dicts
    s = set()

    for num in arr: #O(n)
        if num in s: # O(1)
            s.remove(num)
        else:
            s.add(num) #O(1)
    # at this point, only element in set is our odd element out
    return list(s)[0] #O(1)



if __name__ == '__main__':
    # Use the main function to test your implementation
    start = time.time()
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    print(f'\nResult calculated in {time.time()-start:.20f} seconds')
    print(f"The odd-number-out is {single_number(arr)}")