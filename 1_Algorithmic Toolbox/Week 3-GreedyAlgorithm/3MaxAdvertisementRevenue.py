#Uses python3

import sys
def max_dot_product(n,a, b):
    #write your code here
    res = 0
    '''
    nega = []
    negb = []
    all = []
    for s in range(len(a)):
        if a[s]< 0:
            nega.append(a[s])
            a.pop(s)
    for c in range(len(b)-1):
        if b[c] < 0:
            negb.append(b[c])
            b.pop(c)
    nega.sort()
    negb.sort()
    a.sort(reverse = True)
    b.sort(reverse = True)
    for i in range(n):
        if i < len(a) and i < len(b):
            respos = a[i] * b[i]
            all.append(respos)
        if i < len(negb) and i < len(nega):
            if len(nega) > 0 and len(negb) > 0:
                resneg = nega[i] * negb[i]
                all.append(resneg)
    all.sort(reverse = True)
    print(all)
    res = sum(all[:n])
    '''
    a.sort(reverse = True)
    b.sort(reverse = True)
    
    for i in range(n):
        if len(a)>0 and len(b)>0:
            if a[0]*b[0] >= a[-1]*b[-1]:
                res += a[0]*b[0]
                a.pop(0)
                b.pop(0)
                
            else:
                res += a[-1]*b[-1]
                a.pop(-1)
                b.pop(-1)
                
    return res

inputn = input()
inputa = input()
inputb = input()
#data = list(map(int, input.split()))
n = int(inputn)
a = [int(x) for x in inputa.split()]
b = [int(y) for y in inputb.split()]
print(max_dot_product( n, a, b))

