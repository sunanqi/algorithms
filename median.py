'''
- Problem:
    Given a stream of numbers, at each number, calculate the median at that time. Finanly sum up all medians
    Note: In this problem, for array with even number of numbers, median here is defined as (k/2)th order statistic. E.g.: [1,2,3,4], median is 2
- Algorithm:
    using two heaps to get median in O(1). each insertion need O(log n)
- time complexity:
    get median: O(1)
    add number: O(log n)
- input:
    a stream of numbers
- output:
    a list of medians, or sum of the list
- detail:

-1 -2 -3
 -4 -5     self.u (negative number)
  -6

  7
 8 9       self.l
10 11 12

keep len(self.u) - len(self.l) = 0 or 1

'''

import heapq
from datetime import datetime as dt

class medianFinder():
    def __init__(self):
        self.u = []
        self.l = []
        self.cnt = 0

    def add_number(self,num):
        self.cnt += 1
        if self.cnt >= 11:
            if -num >= self.u[0]:
                heapq.heappush(self.u, -num)
                if len(self.u)-len(self.l)==2:
                    heapq.heappush(self.l, -heapq.heappop(self.u))
            else:
                heapq.heappush(self.l, num)
                if len(self.u)-len(self.l)==-1:
                    heapq.heappush(self.u, -heapq.heappop(self.l))
            return self.get_median()
        elif self.cnt <= 10:
            self.u.append(num)
            self.u.sort()
            # print(self.u, self.cnt)
            median = self.u[(self.cnt-1)//2]
            if self.cnt == 10:
                self.l = self.u[5:]
                self.u = [-i for i in self.u[:5]]
                heapq.heapify(self.l)
                heapq.heapify(self.u)
            return median

    def get_median(self):
        return -self.u[0]


with open('Median.txt') as f:
    lines = f.read().split('\n')

test = medianFinder()
medians = [test.add_number(int(i)) for i in lines if i]
print(sum(medians))
# result is 46831213
