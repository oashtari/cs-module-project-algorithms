'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    new_arr = []
    zero_arr = []

    for i in range(len(arr)):
    # solution 1
        if arr[i] == 0:
            # arr.pop(i)
            zero_arr.append(0)
        if arr[i] != 0:
            new_arr.append(arr[i])
    return new_arr + zero_arr
    # print('new arr', new_arr)
    # print('zero', zero_arr)

    # solution 2
        # if arr[i] == 0:
        #     print('arr', arr)
        #     print('i', i)
        #     arr.insert(len(arr)-1,arr.pop(i))
        #     # print('what is I', arr.pop(i))
            # print('new arr', arr)
            # arr.pop(i)
            # print(i)
        # else:
        #     return arr
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    arr2 = [4, 2, 1, 5]
    arr3 = [0, 0, 0, 0, 3, 2, 1] 

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr2)}")
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr3)}")
    