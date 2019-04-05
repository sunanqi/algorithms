'''
- Problem:
    Given an undirected, unweighted, connected graph, a "cut" is a partition of the vertices. We want to find the partition that has minimal edges between these two partitions.
- Algorithm:
    Karger's (original) randomized algorithm. It can guarantee the lower bound of probability of finding the correct min cut: 2/(n(n-1)).
    By running (n choose 2)*ln n times, the probability of not finding min cut is <= 1/n
    ref: https://www.cs.princeton.edu/courses/archive/fall13/cos521/lecnotes/lec2final.pdf
    ref: https://en.wikipedia.org/wiki/Karger%27s_algorithm#cite_note-simplemincut-2
- time complexity:
    depend on implementation.
    1) Easiest implementation need O(n^2) running time, where n = |V|. (As in the following codes)
    2) using an algorithm similar to Kruskal’s MST need O(m log m) time, where m = |E|
    3) The best known implementations use O(|E|) time and space
- input:
    - graph represented as adjacency lists: g = {vertex : [vertices connected to vertex]}
    - number of repetition
- output:
    a partition of vertices and its min cut
- TODO:
    code runs slow, need optimize
'''

import random
import math
import collections
import datetime

def min_cut_karger(g):

    def find(v):
        if p[v]==v:
            return v
        stack=[]
        while p[v]!=v:
            stack.append(v)
            v = p[v]
        while stack:
            v0 = stack.pop()
            p[v0] = v
        return v

    def contraction(): # one step of contraction
        n_edges = sum(len(g[i]) for i in g)
        offset = random.randint(0, n_edges-1) # generate integer between 0 and n_edges-1, both end inclusive
        for k, v in g.items():
            if offset < len(v):
                vertices_to_contract = (k, v[offset])
                break
            else:
                offset -= len(v)

        v1, v2 = vertices_to_contract
        v1, v2 = find(v1), find(v2)
        #print(v1,v2)
        #print('v1,v2,g[v1],g[v2]', v1,v2,g[v1],g[v2])
        if v1 > v2:
            v1, v2 = v2, v1
        p[v2] = v1
        g[v1] = [find(i) for i in g[v1] if find(i)!=v1] + [find(i) for i in g[v2] if find(i)!=v1]
        del g[v2]
        # return g

    p = {i:i for i in g.keys()}
    while len(g)>2:
        contraction()
    #print(g)
    #print(p)
    #partition = collections.defaultdict(list)
    #for k,v in p.items():
        #partition[find(v)].append(k)
    return len(next(iter(g.values()))) #, partition.values()

if __name__ == '__main__':
    g0 = {}
    with open('kargerMinCut.txt') as f:
        lines = f.read().split('\n')
    for line in lines:
        if line:
            tmp = [int(i) for i in line.split('\t') if i]
            g0[tmp[0]] = tmp[1:]

    print(datetime.datetime.now())
    min_cut, partition = None, None
    # n_repetition = int(len(g0)**2 * math.log(len(g0))+1)
    n_repetition = int(len(g0)) #**2
    print('n_repetition', n_repetition)
    # print(g0)
    for i in range(n_repetition):
        g = g0.copy()
        curr_min_cut = min_cut_karger(g) # curr_partition
        # print(i, curr_min_cut)
        if not min_cut or curr_min_cut < min_cut:
            min_cut = curr_min_cut
            print(min_cut)#, partition)
            # partition = curr_partition
    print(datetime.datetime.now())
