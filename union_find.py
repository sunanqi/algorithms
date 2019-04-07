"""
- Problem:
    Given a set of elements (can be numbers, nodes, etc...), and a list of "connections" of two elements,
    where such connections satisfies Transitive Law, we would like to know how the entire set is partitioned
- Algorithm:
    Union-find data structure, aka disjoint-set data structure
    optimization:
        - path compression
        - union by rank or union by size
        note: rank of element does not change after path compression. that's why it's called rank instead of tree height/depth
- time complexity:
    use both path compression and union by rank (or by size), amortized time per operation is O(alpha(n)), where alpha(n) is inverse Ackermann function
    Since alpha(n)<5 for any value of n that can be written in this physical universe, it's literally O(1) per operation
- input:
    a list of elements, and union_by method
- output:
    all disjoint sets
"""

import collections
class union_find:
    def __init__(self, elements, union_by = 'rank'):
        self.d = {}
        self.union_by = union_by
        for e in elements:
            self.d[e] = [e, 1]  # (leader, rank or size)

    def find(self, e):
        if self.d[e][0] != e:
            self.d[e][0] = self.find(self.d[e][0])
        return self.d[e][0]

    def union(self, e1, e2):
        e1, e2 = self.find(e1), self.find(e2)
        if e1 != e2:
            if self.union_by == 'rank':
                if self.d[e1][1] > self.d[e2][1]: # if e1 has higher rank, e1 becomes new leader
                    self.d[e2][0] = e1
                elif self.d[e1][1] < self.d[e2][1]: # if e2 has higher rank, e2 becomes new leader
                    self.d[e1][0] = e2
                else:  # same rank, then either can be new leader by rank += 1
                    self.d[e1] = self.d[e2] = [e1, self.d[e1][1]+1]
            else: # union by size
                if self.d[e1][1] >= self.d[e2][1]: # if e1 has larger size, e1 becomes new leader
                    self.d[e1] = self.d[e2] = [e1, self.d[e1][1]+self.d[e2][1]]
                else:
                    self.d[e1] = self.d[e2] = [e2, self.d[e1][1]+self.d[e2][1]]
        print(self.d)

    def print_disjoint_sets(self):
        s = collections.defaultdict(set)
        for k,v in self.d.items():
            s[self.find(k)].add(k)
        for k in s:
            print(s[k])
        print(self.d)

if __name__ == '__main__':
    elements = union_find([i for i in range(10)], union_by='size')
    elements.union(0,1)
    elements.union(1,8)
    elements.union(0,2)
    elements.union(3,5)
    elements.union(5,8)
    elements.union(6,9)
    elements.print_disjoint_sets()
