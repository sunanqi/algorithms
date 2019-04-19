"""
- Problem:
    Given a list of numbers (can be negative), choose a sub-sequence without two adjacent numbers that has max sum.
- Algorithm:
    dynamic programming: if we have solved for the first n-1 numbers, for n-th number, we have 2 choices:
    #   1) we do not choose this number, then mwis of first n = mwis of first n-1
    #   2) we do choose this number, then mwis of first n = mwis of first n-2 + weight of n
- time complexity:
    O(n)
- input:
    - a list of weights
- output:
    a list of [mwis for the first i numbers, if this number will be include in the total wmis]
"""

from datetime import datetime as dt
def mwis(W):
    # W: a list of weights
    if len(W)==1:
        return max(W[0], 0)
    if len(W)==2:
        return max(W[0], W[1], 0)
    # W has at least 3 elements
    dp = [[0, None]]
    if W[0]>0:
        dp.append([W[0], True])
    else:
        dp.append([0, False])
    # if we have solved for the first n-1 numbers, for n-th number, we have 2 choices:
    #   1) we do not choose this number, then mwis of first n = mwis of first n-1
    #   2) we do choose this number, then mwis of first n = mwis of first n-2 + weight of n
    for i in range(1, len(W)):
        if dp[-1][0] > dp[-2][0] + W[i]:
            dp.append([dp[-1][0], False])
        else:
            dp.append([dp[-2][0] + W[i], True])
    for i in range(len(dp)-1, 0, -1):
        if dp[i][1] == True:
            dp[i-1][1] = False
    return dp

if __name__ == '__main__':
    start_read_file = dt.now()
    with open('mwis.txt') as f:
        lines = f.read().split('\n')
    W = []
    first_line = True
    for line in lines:
        if first_line:
            first_line = False
        else:
            if line:
                W.append(int(line))
    finish_read_file = dt.now()
    print('read file uses ', finish_read_file-start_read_file, 'seconds')
    print('There are', len(W), 'nodes')
    mw = mwis(W)
    print(mw[-1])  # [2955353732, True]
    print(sum(W[i-1] for i in range(1, len(mw)) if mw[i][1])) #2955353732
    print([mw[i][1] for i in [1, 2, 3, 4, 17, 117, 517, 997]])
    # [True, False, True, False, False, True, True, False]
