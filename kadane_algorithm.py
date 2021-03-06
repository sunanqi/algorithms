'''
Kadane's algorithm to calculate max subarray.

- Problem:
    Given an array (can have both positive and negative numbers), find the subarray that have max sum
- Algorithm:
    for each index i, consider max subarray that ending in i,
    there are two cases:
        1) the number nums[i] itself;
        2) subarray ending in i with at least 2 elements. In this case, we should choose
            the max subarray ending in i-1
- Complexity:
    O(n)
- input:
    list[int]
- output:
    int: maximal sum of subarray of any length
Todo: read https://en.wikipedia.org/wiki/Maximum_subarray_problem
understand this: For 2-dimentional problem, slightly faster algorithms based on distance matrix multiplication have been proposed
'''

def max_subarray(nums):

    if not nums:
        raise Exception('empty array')

    res, max_subarray_ending_in_i = nums[0], 0
    for i, num in enumerate(nums):
        max_subarray_ending_in_i = max(nums[i], max_subarray_ending_in_i+nums[i])
        res = max(res, max_subarray_ending_in_i)

    return res

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] # 6
    print(max_subarray(nums))
