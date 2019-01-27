# Uses python3
import sys
import itertools
A = [3,6,4,5,2,6,5,1,7]
#A = [3,3,5,1,2,4]
x = 3
p = sum(A) // x
n = 0
s = [0 for i in range(len(A))]

def partition3(A):
    if sum(A) % x == 0:
        init = [[0 for x in range(p + 1)] for x in range(len(A) + 1)]
        for i in range(1,len(A) + 1):
            for j in range(1,p + 1):
                init[i][j] = init[i-1][j]
                if j >= A[i-1]:
                    val = init[i-1][j-A[i-1]] + A[i-1]
                    if val > init[i][j]:
                        init[i][j] = val
        if init[-1][-1] != p:
            return 0
        else:
            return init
init = partition3(A)
print('init:', init)
def traceBack(i,j):
    global s   
    if init == 0 or init == None:
        return 0
    else:
        if i== 0 and j == 0:
            print('s:',s)
            return s
        if init[i][j] == init[i-1][j]:
            traceBack(i-1,j)
        
        elif init[i][j] == init[i-1][j-A[i-1]]+A[i-1]:
            s[i-1] = 1
            traceBack(i-1,j-A[i-1])
    

def change():
    global A
    B = []
    if traceBack(len(A),p) == 0:
        return 0
    else:
        for i in range(len(s)):
            if s[i] != 1:
                B.append(A[i])
    A = B

for i in range(3):
    print('A',A)
    init = partition3(A)
    print('init',init)
    if change() != 0:
        n += 1
    s = [0 for i in range(len(A))]
    if x >1:
        x -= 1
    print('p',p,x)
    p = sum(A) // x
        
 
if n == 3:
    print('True')
else:
    print('False')