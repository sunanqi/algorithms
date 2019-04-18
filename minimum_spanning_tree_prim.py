"""
- Problem:
    Given a connected, undirected graph with weighted edge (can be negative),
    find the minimum spanning tree (MST). A MST is a subset of original edges
    that connects all vertices, is acyclic, and have the minimum total weights (lengths)
- Algorithm:
    Prim's algorithm for the follwing codes. Time complexity O(V*logE)
    Some other well-known algorithms:
        - Kruskal's algorithm: O(V*logE)
        - Linear time randomized algorithm (Karger, Klein & Tarjan (1995)): O(V)
        - fastest non-randomized comparison-based algorithm: O(V*inverse Ackermann)
- time complexity:
    O(V*logE) by using heap
- input:
    - original graph represented as adjacency list: G[node1] = [(node2, length_1_2), (node3, length_1_3), ...]
    - set of all nodes
- output:
    a list of tuples [(length_a_b, a, b), (length_a_c, a, c), ...]
"""

import heapq
import collections
from datetime import datetime as dt

def mst_prim(G, nodes): #
    n_nodes = len(nodes)
    res = []
    v = nodes.pop()
    h = []  # (path length, vertex)
    while len(res) < n_nodes-1:
        for w, length in G[v]:
            if w in nodes:
                heapq.heappush(h, (length, v, w))
        while 1:
            length, v, w = heapq.heappop(h)
            if w in nodes:
                nodes.remove(w)
                res.append((length, v, w))
                v = w
                break
    return res

if __name__ == '__main__':
    start_read_file = dt.now()
    with open('edges.txt') as f:
        lines = f.read().split('\n')
    first_line = True
    G = collections.defaultdict(list)
    nodes = set()
    for line in lines:
        if first_line:
            first_line = False
        else:
            if line:
                t, h, l = line.split()
                G[t].append((h,int(l)))
                G[h].append((t,int(l)))
                nodes.add(t)
                nodes.add(h)
    finish_read_file = dt.now()
    print('read file uses ', finish_read_file-start_read_file, 'seconds')
    print('There are', len(nodes), 'nodes and', sum(len(G[k]) for k in G), 'edges')
    res = mst_prim(G, nodes)
    finish_calculating_mst = dt.now()
    print('calculating mst uses', finish_calculating_mst-finish_read_file, 'seconds')
    print(len(res))
    print(sum(i[0] for i in res)) #-3612829
