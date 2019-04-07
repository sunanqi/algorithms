"""
- Problem:
    Given a set of points on 2-d plane, find the pair with smallest (Euclidean) distance.
- Algorithm:
    divide and conquer
    ref: https://www.coursera.org/learn/algorithms-divide-conquer/lecture/nf0jk/o-n-log-n-algorithm-for-closest-pair-i-advanced-optional
- time complexity:
    O(n log n)
- input:
    list[tuple]: n points
- output:
    list[tuple]: 2 points
"""

import itertools
import random

def closest_pair(points):

    def dist(p1, p2):
        return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2

    def brute_force(Px):
        all_pairs = itertools.combinations(Px, 2)
        min_pair = min(all_pairs, key=lambda pair: dist(pair[0], pair[1]))
        return (min_pair[0], min_pair[1], dist(min_pair[0], min_pair[1]))

    def helper(Px, Py):
        if len(Px)<8:
            return brute_force(Px)

        mid = len(Px)//2
        Qx, Rx = Px[:mid], Px[mid:]
        Qy, Ry = [p for p in Py if p in Qx], [p for p in Py if p in Rx]

        (p1,q1,d1) = helper(Qx,Qy)
        (p2,q2,d2) = helper(Rx,Ry)
        delta = min(d1,d2)
        midpoint = max([p[0] for p in Qx])
        Sy = [p for p in Py if p[0] > midpoint-delta and p[0] < midpoint+delta]
        (p3,q3,d3) = closest_split_pair(Sy, delta)

        return min([(p1,q1,d1),(p2,q2,d2),(p3,q3,d3)], key = lambda x:x[2])

    def closest_split_pair(Sy, delta):
        res = (None, None, delta)
        for i in range(len(Sy)):
            j = i+1
            while j<len(Sy) and Sy[j][1]-Sy[i][1]<delta: # only consider y-coordinate of point j and i smaller than delta.
                # according to proof, we look at most 7 points after i
                d = dist(Sy[i], Sy[j])
                if d < res[2]:
                    delta = d
                    res = (Sy[i], Sy[j], d)
                j+=1
        return res

    Px = sorted(points)    # sort by x-coordinate
    Py = sorted(points, key = lambda x: (x[1],x[0]))   # sort by y‐coordinate
    return helper(Px, Py)

if __name__ == '__main__':
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    points = set()
    random.seed(327)
    for i in range(1000):
        point = (random.randint(1,1000), random.randint(1,1000))
        if point not in points:
            points.add(point)
    points = list(points)
    print(closest_pair(points))
