"""
:type num1, num2: str type of an int
:rtype: str type of an int
"""

'''
- Problem:
    Multiply two numbers with a method that is faster than our usual multiplication
- Algorithm:
    WLOG, we assume num1 < num2. Also let n = len(num1)//2, i.e., roughly half of the length of num1 (the smaller one)
    Divide string num1 and num2 to two parts each: num1 = A B and num2 = C D, where A and C are the first n digits.
    Now num1*num2 can be re-written as:
        (10^n*A + B)*(10^n*C + D) = 10^2n*AC + 10^n*(AD+BC) + BD
    Key part!!!:
    In order to get AC, BD and AD+BC, we only need to calculate:
        (1) AC
        (2) BD
        (3) (A+B)(C+D) = AC+BD+AD+BC
    AD+BC can be obtained by (3)-(1)-(2).
- Time complexity:
    if both numbers have n digits, time complexity is O(n ** (log_2^3)) = O(n^1.58)
- input:
    two string type of numbers
- output:
    one string type of numbers
'''

def karatsuba(num1, num2):

    if len(num1)<=1 or len(num2)<=1:
        return str(int(num1)*int(num2))

    if len(num1)>len(num2) or (len(num1)==len(num2) and num1>num2):
        num1, num2 = num2, num1

    n=len(num1)//2
    a,b = num1[:-n], num1[-n:]
    c,d = num2[:-n], num2[-n:]
    #print('a,b,c,d=',a,b,c,d)
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    abcd = karatsuba(str(int(a)+int(b)), str(int(c)+int(d)))
    adbc = str(int(abcd)-int(ac)-int(bd))
    r = int(ac+'0'*(2*n))+int(adbc+'0'*n)+int(bd)
    #print('r=', r)
    return str(r)

n1 = '3141592653589793238462643383279502884197169399375105820974944592'
n2 = '2718281828459045235360287471352662497757247093699959574966967627'
# 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
print(karatsuba(n1, n2))
