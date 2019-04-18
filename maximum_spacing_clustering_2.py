"""
- Problem:
    Find maximum spacing clustering.
    For a graph with positive weighted edges, cluster these points to pre-specified k clusters. We need to maximize the shortest distance between vertices from different clusters
    We are given 200k nodes, each node is a 24 bits binary array. Distance is defined as Hamming distance.
    We want to cluster these nodes as less as possible to make the spacing is at least 3. That is, cluster all pairs of nodes that have Hamming distance 0, 1 or 2.
- Algorithm:
    High level: Compare all pairs of nodes and cluster them if their Hamming distance <= 2
    Detail: traverse array. For each 24-bits binary number, generate its neighbors that are 1 Hamming distance from it. Look up this number and its all neighbors in previous numbers and their neighbors.
        As long as there are any matching, it means there are pairs with Hamming distance at most 2. Cluster them.
- time complexity:
    O(n). (Or O(n_bits * n) if n_bits is also an input)
- input:
    a list of strings = [(1 1 1 0 0 0 0 0 1 1 0 1 0 0 1 1 1 1 0 0 1 1 1 1), (1 1 1 0 0 0 0 0 1 1 0 1 0 0 1 1 1 1 0 0 1 1 1 0), ...]
- output:
    Number of clusters.
    Or if need more details, a list of all disjoint sets (equivalence class): [{1,2,3}, {4,5},...]
"""

import collections
import itertools
from datetime import datetime as dt
import union_find  # self-defined class, put union_find.py in the same directory

def maximum_spacing_clustering(nodes, n_bits):
    # nodes: set {1,2,3....}.
    # connect all nodes pairs with distance <= 2
    # return number of clusters and a list of cluster members
    #def get_bit_value(num, position):
    #    # check if the n-th position of num is 1 (0-th position is the least significant digit)
    #    return (num & (1 << position)) > 0

    def set_value(num, position, value):
        # set the n-th position of num to the specified value.
        mask = 1 << position   # Compute mask, an integer with just bit 'index' set.
        num &= ~mask          # Clear the bit indicated by the mask
        if value:
            num |= mask         # If value was 1/True, set the bit indicated by the mask.
        return num

    def get_neighbors(num, n_bits):
        # generate "neighbors" that differ at at most [distance] positions of bit representation
        # return [set_value(num,i,0)+set_value(num,i,1)-num for i in range(n_bits)]
        tmp = [set_value(num,i,j) for i in range(n_bits) for j in (0,1)]
        return [i for i in tmp if i!=num]

    G = union_find.union_find(nodes)
    all_nodes = collections.defaultdict(list, {i:[i] for i in nodes})
    for num in nodes:
        neighbors = get_neighbors(num, n_bits)
        for nei in neighbors:
            if nei in all_nodes:
                for i in all_nodes[nei]:
                    G.union(num, i)
            all_nodes[nei].append(num)
    return G.print_disjoint_sets()

if __name__ == '__main__':
    with open('clustering_big.txt') as f:
        lines = f.read().split('\n')
    nodes = []
    first_line = True
    for line in lines:
        if first_line:
            n_bits = int(line.split()[1])
            first_line = False
        else:
            if line:
                nodes.append(int(line.replace(' ',''), base=2))
    print(n_bits)  #24
    print(len(nodes))  #200000
    print(len(set(nodes)))   #198788
    print(dt.now())
    print(len(maximum_spacing_clustering(nodes, n_bits)))  #6118
    print(dt.now())
    # print(nodes[:5]) # [14734287, 6709165, 7344869, 15449752, 5157860]
    #l, disjoint_sets = maximum_spacing_clustering(nodes, 4, edges)
    #print(l) # maximum spacing = 106
    #print([len(i) for i in disjoint_sets])  # 4 clusters with size 497, 1, 1, 1 respectively
