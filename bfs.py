"""
- Problem:
    traverse nodes in a graph
- Algorithm:
    BFS
- time complexity:
    O(V+E)
    optimization: before bfs, convert adjacency list to iterator
- input:
    graph represented as adjacency list
- output:
    reachable nodes
"""

import collections
import datetime
def bfs(G, s):
    for k in G:
        G[k] = iter(G[k])
    explored = set([s])
    queue = collections.deque()
    queue.append(G[s])
    while queue:
        try:
            v = next(queue[0])
            if v not in explored:
                explored.add(v)
                queue.append(G[v])
        except:
            queue.popleft()
    return explored

if __name__ == '__main__':
    start_read_file = datetime.datetime.now()
    G = collections.defaultdict(list)
    with open('SCC.txt') as f:
        lines = f.read().split('\n')
    for line in lines:
        if line:
            tmp = [int(i) for i in line.split()]
            G[tmp[0]].append(tmp[1])
    finish_read_file = datetime.datetime.now()
    print('read file uses ', finish_read_file-start_read_file, 'seconds')
    print('total number of nodes:', len(G))
    print('number of reachable nodes:', len(bfs(G,1)))
    finish_bfs = datetime.datetime.now()
    print('bfs uses ', finish_bfs - finish_read_file, 'seconds')
