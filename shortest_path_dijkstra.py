"""
- Problem:
    calculate shortest path of a non-negative directed graph from a single start point
- Algorithm:
    Dijkstra algorithm with heap
- time complexity:
    O (E log V)
    optimization: Note: using Fibonacci Heap may be faster
- input:
    dict of dict
    {tail1: {head1:length,
            lead2:length},
     tail2: ...}
- output:
    a dict of ending point : distance
"""

import datetime
import heapq
import collections

def Dijkstra(G, nodes, s): # graph, nodes, start point
    sp = {v:None for v in nodes}
    h = [(0, s)]   #  (path length, vertex)
    while h:
        path_len, v = heapq.heappop(h)
        if not sp[v]:  # v's shortest path has not been calculated yet
            sp[v] = path_len
            for w, edge_len in G[v].items():
                if not sp[w]:
                    heapq.heappush(h, (path_len + edge_len, w))
    return sp

if __name__ == '__main__':
    start_read_file = datetime.datetime.now()
    G = collections.defaultdict(dict)
    nodes = set()
    with open('dijkstraData.txt') as f:
        lines=f.read().split('\n')
    for line in lines:
        if line:
            tmp = line.split()
            G[int(tmp[0])].update({int(v.split(',')[0]):int(v.split(',')[1]) for v in tmp[1:]})
            nodes.add(int(tmp[0]))
            nodes |= set({int(v.split(',')[0]) for v in tmp[1:]})
    finish_read_file = datetime.datetime.now()
    print('read file uses ', finish_read_file-start_read_file, 'seconds')
    print('total number of nodes:', len(nodes))
    print('total number of edges:', sum(len(G[k]) for k in G))
    ShortestPath = Dijkstra(G,nodes,1)
    print([ShortestPath[i] for i in [7,37,59,82,99,115,133,165,188,197]])
    finish_calculating_shortest_path = datetime.datetime.now()
    print('calculating shortest path uses ', finish_calculating_shortest_path - finish_read_file, 'seconds')
