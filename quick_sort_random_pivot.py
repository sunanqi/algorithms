"""
- Problem:
    sort an array
- Algorithm:
    1. Select a pivot. If random_pivot == True, a random number is selected as pivot, otherwise the first number is pivot
    2. swap numbers in the array until left part is all <= pivot and right part is all > pivot
    3. recurse to sort the left part and right part
- time complexity:
    For random pivot, O(n logn) on average, where average is over the random choices. Worst case can be O(n^2)
- input:
    list[int]
- output:
    list[int]
"""

import random
def quicksort(nums, random_pivot=True):

    def helper(st, ed):
        # print(st,ed)
        if st+1 >= ed:
            return
        # work on nums[st:ed] (not including ed)
        if random_pivot:
            pivot = random.randint(st,ed-1)
            nums[st], nums[pivot] = nums[pivot], nums[st]
        pivot = nums[st]
        p1, p2 = st+1, ed-1
        while True:
            while p1<ed and nums[p1] <= pivot:
                p1 += 1
            while nums[p2] > pivot:
                p2 -= 1
            '''
            pivot st+1 ... ed-1 ed
                3    1 2 3    4  5
            after here, st=4, ed=3
            pivot st+1 ... ed-1 ed
                3    1 2 4    2  5
            after here, st=4, ed=2
            '''
            if p1>p2:
                break
            nums[p1], nums[p2] = nums[p2], nums[p1]
        nums[st], nums[p2] = nums[p2], nums[st]
        helper(st, p2)
        helper(p1, ed)

    helper(0, len(nums))
    return nums

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(quicksort(nums, random_pivot=True))
