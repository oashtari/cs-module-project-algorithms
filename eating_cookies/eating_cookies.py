'''
Input: an integer
Returns: an integer
'''
# what is runtime and why is it slow? O(3**n)
# using caching/memoization, runtime is now O(n)
def eating_cookies(n, cache=None):
    # Your code here
    # what are base case(s)
    if n < 0: # if negative
        return 0

    # represents there being x number cookies, we can take all of them
    elif n == 0:
        return 1

    # check cache to see if answer is stored in there
    elif cache and cache[n] > 0:
        return cache[n]

    else:
        if not cache:
            # initialize an empty cache
            # using dict comprehension
            cache = {i: 0 for i in range(n+1)}
        # store answers in our cache
        
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")



# FIND SMALLEST MISSING
# can binary search help us here?
# binary search requires us to know our target

# using binary search improved O(n) to O(log n)

# 1. find midpoint
# 2. check if midpoint element matches its index
# 3. when we've narrowed search space down to 2 elements, we can always return the larger/right one

def find_smallest_missing(arr):
    # if arr is not sorted, can run arr.sort(), but that has a O(n log n) which is expensive
    if arr[0] !=0:
        return 0

    # add another check if arr[-1] == len(arr) -1, checks to see if nothing is missing
    if arr[-1] == len(arr) - 1:
        return len(arr)

    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        if arr[mid] == mid:
            # toss out left side
            # don't include midpoint as it matches its index
            start = mid + 1

        else:
            # toss out the right side, but do keep the midpoint
            # since cannot rule out that is the smallest missing
            end = mid

    # we've narroed it down to one element
    # at this point start == end, so return either
    return end

    # O(n) traverals through entire array
    # realizing that we're not taking advantage of fact that input is sorted,
    # we can ask ourselves how to leverage that fact ()
    for i in range(len(arr) - 1):
        if arr[i+1] != arr[i] + 1:
            return arr[i] + 1

    return arr[-1] + 1

A1 = [0,1,2,6,9,11,15]
A2 = [1,2,3,4,6,9,11,15]
A3 = [0,1,2,3,4,5,6]

print(find_smallest_missing(A1))
print(find_smallest_missing(A2))
print(find_smallest_missing(A3))


"""
Techniques for improving efficiency
1. take advantage of all available information
2. ensuring we're using the most appropriate data structure
3. caching/memoization -- 
3a. save work that's already been done
3b. how do we save it
3c. how do we make it available for all the recursive calls
"""