'''
- Problem:
    We have a list of N numbers, so we have (N choose 2) ways of selecting 2 different numbers from this list (difference in index, values can be the same).
    Out of these (N choose 2) pairs, how many pairs are inversion, i.e., (i,j) such that i<j but A[i]>A[j]
- Algorithm:
    use divide and conquer: for each sub-problem, we not only count number of inversions, but also sort the list
- complexity:
    O (n * log n)
- input: list[int]
- output: num of inversions
'''

def countInversion(array):

    def helper(l):
        '''
        input: list
        output: num of inversions and sorted list
        '''
        if len(l)==1:
            return 0, l
        if len(l)==2:
            return (1 if l[0]>l[1] else 0, [min(l), max(l)])
        n = len(l)

        inv1, l1 = helper(l[:n//2]) # num of inversions and sorted list of left half part
        inv2, l2 = helper(l[n//2:]) # num of inversions and sorted list of right half part

        # calculate inversions between left and right part
        p1, p2 = 0, 0
        inv = inv1+inv2
        merged_list = []

        while p1<len(l1) and p2<len(l2):
            if l1[p1] <= l2[p2]:
                merged_list.append(l1[p1])
                p1 += 1
            else:
                merged_list.append(l2[p2])
                p2 += 1
                inv = inv + (len(l1)-p1)

        if p1<len(l1):
            merged_list += l1[p1:]
        else:
            merged_list += l2[p2:]

        return inv, merged_list

    return helper(array)[0]

array = [6,4,5,3,1,2] # 5+3+3+2=13
array = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45] #590
array = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]  #2372
# with open('IntegerArray.txt') as f:
#     p=f.read().split('\n')
# q = [int(i) for i in p if len(i)]
print(countInversion(array))
