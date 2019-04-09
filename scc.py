"""
- Problem:
    find Strongly Connected Components in a directed graph
- Algorithm:
    Kosaraju’s algorithm

    For the dfs function inside main function, it works like this:
        1. Besides taking graph and nodes as input, it also needs an ordered list of nodes.
        2. it reads from the last node, starts from this node and runs dfs, and records nodes based on finish time
        3. all the nodes reachable from the above (last) node form a list.
        4. then we continue to search the original ordered list of nodes backward, and as long as there are any nodes
            not explored yet, we dfs from this node, and form a new list of reachable nodes (based on finish time)
        5. finally the output is multiple lists of nodes, in the form of list of list of nodes

    We start the ordered_nodes by list(set of all nodes). Order does not matter.
    First run of dfs gives us finish time, grouped by "leader"
    Second run gives us scc, grouped by leader

- time complexity:
    O(V+E)
- input:
    original graph represented as adjacency list
    reversed graph
    set of all nodes
- output:
    a list of list of nodes
    [[node1, node2,...], [node3, node4,...],...]
    each list inside the list is a SCC
"""

import collections
import datetime
def scc(G, Grev, all_nodes):

    def dfs(G, nodes, ordered_nodes):
        # input ordered nodes: [[4,5,3], [0,2,1]]
        nodes_ordered_by_finish_time = []
        while ordered_nodes:
            if not ordered_nodes[-1]:
                ordered_nodes.pop()
                continue
            s = ordered_nodes[-1].pop()
            if s not in nodes:
                continue
            nodes.remove(s)
            stack = [(s, G[s])]
            nodes_ordered_by_finish_time.append([])
            while stack:
                # print(stack)
                try:
                    v = next(stack[-1][1])
                    if v in nodes:
                        nodes.remove(v)
                        stack.append((v, G[v]))
                except:
                    nodes_ordered_by_finish_time[-1].append(stack.pop()[0])
        return nodes_ordered_by_finish_time

    ordered_nodes = [list(all_nodes)]
    nodes = all_nodes.copy()
    ordered_nodes = dfs(G, nodes, ordered_nodes)
    nodes = all_nodes.copy()
    ordered_nodes = dfs(Grev, nodes, ordered_nodes)
    return ordered_nodes

if __name__ == '__main__':
    start_read_file = datetime.datetime.now()
    G = collections.defaultdict(list)
    Grev = collections.defaultdict(list)
    all_nodes = set()
    with open('SCC.txt') as f:
        lines = f.read().split('\n')
        for line in lines:
            if line:
                tail, head = [int(i) for i in line.split()]
                G[tail].append(head)
                Grev[head].append(tail)
                all_nodes.add(tail)
                all_nodes.add(head)
    for k in G:
        G[k] = iter(G[k])
    for k in Grev:
        Grev[k] = iter(Grev[k])
    finish_read_file = datetime.datetime.now()
    print('read file uses ', finish_read_file-start_read_file, 'seconds')
    scc = scc(G, Grev, all_nodes)
    finish_calculating_scc = datetime.datetime.now()
    print('calculating scc uses ', finish_calculating_scc-finish_read_file, 'seconds')
    scc.sort(key = lambda x:len(x), reverse = True)
    sort_scc = datetime.datetime.now()
    print('sort scc uses ', sort_scc - finish_calculating_scc, 'seconds')
    print([len(i) for i in scc[:5]])
