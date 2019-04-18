import heapq
import collections
from datetime import datetime as dt
import union_find  # self-defined class, put union_find.py in the same directory

def mst_kruskal(edges, nodes): #
    heapq.heapify(edges)
    G = union_find.union_find(nodes)
    res = []
    for i in range(len(nodes)-1):
        while 1:
            length, v, w = heapq.heappop(edges)
            if G.union(v,w):
                res.append((length, v, w))
                break
    return res

if __name__ == '__main__':
    start_read_file = dt.now()
    with open('edges.txt') as f:
        lines = f.read().split('\n')
    first_line = True
    edges = []
    nodes = []
    for line in lines:
        if first_line:
            first_line = False
        else:
            if line:
                t, h, l = line.split()
                edges.append((int(l),t,h))
                nodes += [t,h]
    nodes = set(nodes)
    finish_read_file = dt.now()
    print('read file uses ', finish_read_file-start_read_file, 'seconds')
    print('There are', len(nodes), 'nodes and', len(edges), 'edges')
    res = mst_kruskal(edges, nodes)
    finish_calculating_mst = dt.now()
    print('calculating mst uses', finish_calculating_mst-finish_read_file, 'seconds')
    print(len(res))
    print(sum(i[0] for i in res)) #-3612829
