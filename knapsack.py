"""
- Problem:
    Classical knapsack problem: given a set of items, each with a weight and a value, determine the number of each item to include
    in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
- Algorithm:
    dynamic programming
- time complexity:
    O(number of items * capacity)
- input:
    int: capacity
    list of int tuple: [(value1, weight1), (value2, weight2), ...]
- output:
    int: total value (max value)
    list of selected items: [(value1, weight1), (value2, weight2), ...]
reference:
    https://www.coursera.org/learn/algorithms-greedy/lecture/LIgLJ/the-knapsack-problem
"""

from datetime import datetime as dt
def knapsack(capacity, items):
    # capacity: int
    # items: list of [value, weight]
    items = [item for item in items if item[0]>0] # remove 0 value items
    stack = [(capacity, len(items)-1)]  # remaining capacity to use, items can be used (i means up to i-th index-ed item can be used)
    m = {} # memory

    while stack:
        if stack[-1] in m:  # already calculated
            stack.pop()
        elif stack[-1][1]==0:  # only 1 item can be used
            if items[0][1] > stack[-1][0]: # the only 1 item is heavier than capacity
                m[stack[-1]] = (0, False)
            else:
                m[stack[-1]] = (items[0][0], True)
            stack.pop()
        else:
            if items[stack[-1][1]][1] > stack[-1][0]: # the last item is too heavy
                if (stack[-1][0], stack[-1][1]-1) in m:
                    m[stack[-1]] = (m[(stack[-1][0], stack[-1][1]-1)][0], False)
                    stack.pop()
                else:
                    stack.append((stack[-1][0], stack[-1][1]-1))
            else:  # we can either select the last item, or not use it
                if ((stack[-1][0], stack[-1][1]-1) in m) and ((stack[-1][0]-items[stack[-1][1]][1], stack[-1][1]-1) in m):
                    if m[(stack[-1][0], stack[-1][1]-1)][0] > m[(stack[-1][0]-items[stack[-1][1]][1], stack[-1][1]-1)][0]+items[stack[-1][1]][0]:
                        m[stack[-1]] = (m[(stack[-1][0], stack[-1][1]-1)][0], False)
                    else:
                        m[stack[-1]] = (m[(stack[-1][0]-items[stack[-1][1]][1], stack[-1][1]-1)][0]+items[stack[-1][1]][0], True)
                    stack.pop()
                else:
                    cap, n = stack[-1]
                    if (cap, n-1) not in m:
                        stack.append((cap, n-1))
                    if (cap-items[n][1], n-1) not in m:
                        stack.append((cap-items[n][1], n-1))

    total_value = m[(capacity, len(items)-1)]
    selected_items = []
    for n in range(len(items)-1, -1, -1):
        if (capacity, n) in m and m[(capacity, n)][1]:
            selected_items.append(items[n])
            capacity -= items[n][1]
            if capacity<=0:
                break
    return total_value[0], selected_items

if __name__ == '__main__':
    start_read_file = dt.now()
    with open('knapsack_big.txt') as f:
        lines = f.read().split('\n')
        first_line = True
        items = []
        for line in lines:
            if first_line:
                capacity, _  = [int(i) for i in line.split()]
                first_line = False
            else:
                if line:
                    items.append([int(i) for i in line.split()])
    finish_read_file = dt.now()
    print('read file uses ', finish_read_file-start_read_file, 'seconds')
    print('There are', len(items), 'items and capacity is', capacity)
    total_value, selected_items = knapsack(capacity, items)
    finish_calculating_knapsack = dt.now()
    print('calculating knapsack used', finish_calculating_knapsack-finish_read_file, 'seconds')
    print('max value is', total_value)
    print('to verify, total value is', sum(i[0] for i in selected_items))
    print('total weight is', sum(i[1] for i in selected_items))

'''
small dataset:
max value is 2493893
total weight is 9976

big dataset:
max value is 4243395
total weight is 1999783
'''
