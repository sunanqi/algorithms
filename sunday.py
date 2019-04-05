'''
- Problem:
    find substring in a string with an efficient way
- Algorithm:
    Sunday algorithm, a variation of Boyer–Moore algorithm
- time complexity:
    best Ω(n/m), worst O(mn). n = string length; m = pattern length
    string search algorithm comparison: https://en.wikipedia.org/wiki/String-searching_algorithm
input:
    string s: long array of strings;
    string p: pattern, normally a short array of string
output:
    int: the first index in s that matchs p. If no matches, return -1
'''

def sunday(s, p):
    '''
    sunday algorithm
    input: s: long array of strings; p: pattern, normally a short array of string
    output: find the first index in s that matchs p. If no matches, return -1
    idea:
    1) start both s and p from the beginning: compare s[0] and p[0], s[1] and p[1], etc...
    2) if any comparison is not matching, move the pointer in s to the end of current comparison, then further move 1 step forward;
       for p, move the pointer to the last letter that is the same as the one pointed in s. If such letter does not exist, point to 0 in p and move pointer in s 1 step forward
    example:
    s =    abcDefc
    p =     bcEef
    In the above example, we found that D != E. Then the pointer in s will be at the next "c"; and the pointer in p will be also at "c":
    s =    abcDefc
    p =         bcEef
    Time complexity: preprocess: Θ(m+k); matching: best Θ(n/m), worst Θ(n*m)
    space complexity: Θ(k)
    m = len(p); n = len(s); k = length of all alphabet
    '''
    if not p:
        return 0
    d = {}
    for i in reversed(range(len(p))):
        if p[i] not in d:
            d[p[i]] = i

    i,j = 0,0
    while i<len(s):
        if s[i]==p[j]:
            i,j = i+1, j+1
            if j==len(p):
                return i-j
        else:
            '''
            suppose i,j=3,2; len(needle=5)
            abcDefc
             bcEef
            need to move 'c' to 'c'
            abcDefc
                 bcEef
            '''
            i += len(p)-j
            if i>=len(s):
                return -1
            if s[i] in d:
                j = d[s[i]]
                i,j = i-j, 0
            else:
                i,j = i+1,0

    return -1

if __name__ == '__main__':
    s, p = 'ABABDABACDABABCABAB', 'ACDA'
    print(sunday(s,p))
