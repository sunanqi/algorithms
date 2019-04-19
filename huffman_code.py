"""
- Problem:
    Given a list of char/nodes/items with corresponding weights, calculate their huffman code, i.e., binary representations that minimize the total (average) length
- Algorithm:
    Huffman's algorithm
    for details please refer to: https://www.coursera.org/learn/algorithms-greedy/lecture/plgXS/introduction-and-motivation
- time complexity:
    O(n log n)
- input:
    dict of {item:weight}
- output:
    dict of {item:huffman_code}
"""

from datetime import datetime as dt
import collections
import heapq

def huffman_code(W):
    # W: dict of {node or char : weight}
    i, h = 1, []
    h_code = collections.defaultdict(str)
    for node, weight in W.items():
        h.append((weight, i, [node]))
        i+=1
    heapq.heapify(h)
    while len(h)>=2:
        w0, _, nd0 = heapq.heappop(h)
        w1, _, nd1 = heapq.heappop(h)
        for nd in nd0:
            h_code[nd] = '0'+h_code[nd]
        for nd in nd1:
            h_code[nd] = '1'+h_code[nd]
        heapq.heappush(h, (w0+w1, i, nd0+nd1))
        i+=1
    return h_code

if __name__ == '__main__':
    start_read_file = dt.now()
    with open('huffman.txt') as f:
        lines=f.read().split('\n')
    i = 0
    W = {}
    for line in lines:
        if i==0:
            i+=1
        else:
            if line:
                W[i] = int(line)
                i+=1
    finish_read_file = dt.now()
    print('read file uses ', finish_read_file-start_read_file, 'seconds')
    print('There are', len(W), 'items')
    h_code = huffman_code(W)
    finish_calculating_huffman_codes = dt.now()
    print('calculating huffman codes uses', finish_calculating_huffman_codes-finish_read_file, 'seconds')
    print('the lengths of huffman codes are', set(len(h_code[i]) for i in h_code))
