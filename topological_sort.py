"""
- Problem:
    Topologically sort a graph
- Algorithm:
    DFS-alike
- time complexity:
    O(V+E)
    optimization: before dfs, convert adjacency list to iterator
- input:
    graph represented as adjacency list
- output:
    if it can be sorted topologically, i.e., acyclic, output an order (any working order)
    otherwise return -1
"""

import collections
import datetime

def toposort(G, nodes):
    order = [None for _ in range(len(nodes))]
    curr_label = len(nodes)-1
    # for k in G:
    #     G[k] = iter(G[k])
    while nodes:
        s = nodes.pop()
        stack = [(s,iter(G[s]))]
        while stack:
            try:
                v = next(stack[-1][1])
                if v in nodes:
                    nodes.remove(v)
                    stack.append((v, iter(G[v])))
            except:
                order[curr_label] = stack.pop()[0]
                curr_label -= 1
                if curr_label == -1:
                    return -1
    return order

if __name__ == '__main__':
    start_read_file = datetime.datetime.now()
    G = collections.defaultdict(list)
    nodes = set()
    with open('SCC.txt') as f:
        lines = f.read().split('\n')
    for line in lines:
        if line:
            tmp = [int(i) for i in line.split()]
            G[tmp[0]].append(tmp[1])
            nodes.add(tmp[0])
            nodes.add(tmp[1])
    finish_read_file = datetime.datetime.now()
    print('read file uses ', finish_read_file-start_read_file, 'seconds')
    print('total number of nodes:', len(nodes))
    print('total number of edges:', sum(len(G[k]) for k in G))
    print('order:', toposort(G, nodes))
    finish_toposort = datetime.datetime.now()
    print('topo sort uses ', finish_toposort - finish_read_file, 'seconds')
