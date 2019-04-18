"""
- Problem:
    Find maximum spacing clustering.
    For a graph with positive weighted edges, cluster these points to pre-specified k clusters. We need to maximize the shortest distance between vertices from different clusters
- Algorithm:
    Greedy algorith to cluster points that belong to different cluster and have least distance
- time complexity:
    O(E log V), assuming union find runs in O(1) time in each loop
- input:
    a list of edges = [(len, tail, head), (len, tail, head), ...]
- output:
    (max spacing, disjoint sets)
"""

import collections
import union_find # self-defined class, put union_find.py in the same directory

def maximum_spacing_clustering(nodes, k, edges):
    # edges = [(len, tail, head), (len, tail, head), ...]
    # return: (max spacing, disjoint sets)
    G = union_find.union_find(nodes)
    if edges:
        edges.sort()
    for (l,t,h) in edges:
        if G.union(t,h):
            k+=1
        if k==len(nodes):
            disjoint_sets = G.print_disjoint_sets()
        if k==len(nodes)+1:
            return l, disjoint_sets


if __name__ == '__main__':
    with open('clustering1.txt') as f:
        lines = f.read().split('\n')
    nodes = set()
    edges = []
    first_line = True
    for line in lines:
        if first_line:
            first_line = False
        else:
            if line:
                t,h,l = line.split()
                nodes.add(t)
                nodes.add(h)
                edges.append((int(l),t,h))
    print(len(edges))  # 124750
    print(len(nodes))  # 500
    l, disjoint_sets = maximum_spacing_clustering(nodes, 4, edges)
    print(l) # maximum spacing = 106
    print([len(i) for i in disjoint_sets])  # 4 clusters with size 497, 1, 1, 1 respectively
