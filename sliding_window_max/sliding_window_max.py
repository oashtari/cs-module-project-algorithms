'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    all_max = []
    for i in range(len(nums)):
        the_max = max(nums[i:k])
        k +=1
        all_max.append(the_max)
        # print('k', )
        # print('i', i)
        # print(nums[i])
    return all_max


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    arr2 = [70, 37, 100, 66, 1, 45, 27, 62, 75, 57, 92, 66, 9, 39, 15, 69, 46, 72, 35]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
    print(f"Output of sliding_window_max function is: {sliding_window_max(arr2, 5)}")
