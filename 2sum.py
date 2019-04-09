"""
- Problem:
    given a list of 1m integers (not necessarily distinct), find target values
    in the interval [-10000,10000] (inclusive) such that there are distinct
    numbers x,y in the input that satisfy x+y = t
- Algorithm:
    1. sort array
    2. for each number in the left half, binary search -10000-num and 10000-num in the array, put the sum in the result
    3. dedup result
- time complexity:
    It could be as bad as O(nlogn + tn) (t is the range -10000,10000)
    However since numbers are sparse, it runs pretty fast. Results are calculated in 2 seconds
- input:
    list[int]
- output:
    set of int
"""
from datetime import datetime as dt
import collections
import bisect

def two_sum(nums, l, u): # set of numbers, lower bound of sum, upper bound of sum
    nums = sorted(list(nums))
    res = []
    for i in range(len(nums)//2+1):
        lb = bisect.bisect_left(nums, l-nums[i])
        ub = bisect.bisect_right(nums, u-nums[i])
        res += [nums[i]+j for j in nums[lb:ub] if j!=nums[i]]
    return set(res)

if __name__ == '__main__':
    start_read_file = dt.now()
    with open('2sum.txt') as f:
        lines=f.read().split('\n')
    nums = set(int(i) for i in lines if i)
    finish_read_file = dt.now()
    print('read file uses ', finish_read_file-start_read_file, 'seconds')
    print('total distinct numbers:', len(nums))
    sums = two_sum(nums, -10000, 10000)
    print(len(sums))
    finish_calculating_2sum = dt.now()
    print('calculating 2 sum uses ', finish_calculating_2sum - finish_read_file, 'seconds')
