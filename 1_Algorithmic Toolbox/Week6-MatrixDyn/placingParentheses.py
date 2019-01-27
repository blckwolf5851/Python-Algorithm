#uses python 3
import math

def min(a,b,c,d): #problem
    min = a
    if b < min:
        min = b
    if c < min:
        min = c
    if d < min:
        min = d
    return min

def max(a,b,c,d): #problem
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    if d > max:
        max = d
    return max

def findMinMax(i,j,m,M):
    mini = 10000000
    maxi = -10000000
    for k in range(i,j):
        if op[k] == '+':   
            a = m[i][k] + m[k+1][j]
            b = m[i][k] + M[k+1][j]
            c = M[i][k] + m[k+1][j]
            d = M[i][k] + M[k+1][j]
        elif op[k] == '-': 
            a = m[i][k] - m[k+1][j]
            b = m[i][k] - M[k+1][j]
            c = M[i][k] - m[k+1][j]
            d = M[i][k] - M[k+1][j]
        elif op[k] == '*': 
            a = m[i][k] * m[k+1][j]
            b = m[i][k] * M[k+1][j]
            c = M[i][k] * m[k+1][j]
            d = M[i][k] * M[k+1][j]
        elif op[k] == '/': 
            a = m[i][k] / m[k+1][j]
            b = m[i][k] / M[k+1][j]
            c = M[i][k] / m[k+1][j]
            d = M[i][k] / M[k+1][j]
        if min(a,b,c,d) < mini:
            mini = min(a,b,c,d)
        if max(a,b,c,d) > maxi:
            maxi = max(a,b,c,d)
    return (mini,maxi)

def final(d,op):
    m = [[0 for i in range(len(d))] for i in range(len(d))]
    M = [[0 for i in range(len(d))] for i in range(len(d))]
    
    for i in range(len(d)):
        m[i][i] = d[i]
        M[i][i] = d[i]
    for s in range(1,len(d)):
        for n in range(1,len(d) + 1 - s):
            j = n + s - 1
            i = n - 1
            m[i][j],M[i][j] = findMinMax(i,j,m,M)
    return M[0][-1]

s = input()
d = []
op = []
#op = ['-','+','*','-','+']
#d = [5,8,7,4,8,9]
for i in list(s):
    if i.isdigit():
        d.append(int(i))
    else:
        op.append(i)
print(final(d,op))