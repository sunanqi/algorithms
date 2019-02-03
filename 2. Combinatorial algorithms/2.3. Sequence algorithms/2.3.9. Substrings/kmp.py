def kmp(s, p):
    '''
    input: s: long array of strings; p: pattern, normally a short array of string
    output: find the first index in s that matchs p. If no matches, return -1
    '''
    '''
    details https://blog.csdn.net/v_july_v/article/details/7041827
    first calculate next array.
    next array is the LPS (longest proper prefix which is also suffix) before this char
    pattern: A B C D A B D E
    LPS:     0 0 0 0 1 2 0 0
    next:   -1 0 0 0 0 1 2 0

    next is calculated using DP:
    suppose we already have next[0], next[1], ... , next[j], and next[j] is k.
    That is, p[0],   p[1],     ..., p[k-1] and
             p[j-k], p[j-k+1], ..., p[j-1] are the same
    for next[j+1]:
    1) if p[k]==p[j]: next[j+1] = k+1
    2) otherwise: since p[j-1]==p[k-1], and in order to find the LPS, we need some element that is equal to p[j-1], which is also p[k-1],
    that means we can further look next[k]. Denote next[k] = l, we have:
    p[0],   ..., p[l-1] and
    p[k-l], ..., p[k-1] and
    p[j-l], ..., p[j-1] are all the same
    So let's compare p[l] and p[j]. If they are the same, then next[j+1]=l+1
    If they are still not the same, then further check next[l].
    If nothing is equal, then next[j+1]=0
    optimization: suppose we have got next[j+1] = a, that means, when we search string s, if p[j+1] and s[i] does not match, we continue to check p[next[j+1]] with s[i].
    when p[j+1] happens to be p[next[j+1]], then we know it's a mismatch
    that means we can let next[j+1] to be next[next[j+1]]
    '''
    if len(p)==1:
        return s.find(p[0])

    # calculate next - preprocess pattern p
    next = [0 for i in range(len(p))]
    next[0] = -1
    for j in range(1,len(p)-1):
        k = next[j]
        while k>-1:
            if p[k]==p[j]:
                next[j+1] = k+1
                break
            else:
                k = next[k]
        if p[j+1]==p[next[j+1]]: # optimization
            next[j+1] = next[next[j+1]]

    '''
    For brute force search, if s[i] and p[j] mismatch, we reset i,j = i - (j - 1)，j = 0
    For KMP, we set i, j = i, next[j]
        0123456789
    s = ABCDACGGGGGGG
    p = ABCDABDE
    when i, j = 5, 5, mismatch is found. next[j] = next[5] = 1, so set j=1.
        0123456789
    s = ABCDACGGGGGGG
    p =     ABCDABDE
    we compare s[5] and p[1]. Mismatch, so we set j=-1. Then in the next while loop, i,j = i+1, j+1, so we continue to compare s[6] and p[0]
        0123456789
    s = ABCDACGGGGGGG
    p =       ABCDABDE
    '''
    i, j = 0, 0
    while i<len(s):
        if s[i]==p[j] or j==-1:
            i, j = i+1, j+1
        else:
            j = next[j]
        if j==len(p):
            return i-j
    return -1


if __name__ == '__main__':
    s, p = 'ABABDABACDABABCABAB', 'ACDA'
    print(kmp(s,p))
