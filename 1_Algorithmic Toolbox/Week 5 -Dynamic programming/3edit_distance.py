# Uses python3
def min(a,b,c):
    mini = a
    if b < mini:
        mini = b
    if c < mini:
        mini = c
    return mini

def ed(A,B):
    D = [[0 for i in range(len(A)+1)] for x in range(len(B)+1)] #2-D array with A as row, B as colum
    
    # put init in first row
    for i in range(len(A)+1):
        D[0][i] = i
    # put init in first colum
    for i in range(len(B)+1):
        D[i][0] = i
    
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            delete = D[j-1][i] + 1
            insert = D[j][i-1] + 1
            match = D[j-1][i-1]
            mismatch = D[j-1][i-1] + 1
            if A[i-1] == B[j-1]:
                D[j][i] = min(delete, insert, match)
            else:
                D[j][i] = min(delete, insert, mismatch)
    return D

def traceBack(i,j):
    global count
    str1 = [[],[]]
    # base case
    D = ed(A,B)
    if i == 0 and j == 0 :
        return
    if  i > 0 and D[j][i-1] + 1 == D[j][i]: #left
        str1[0].append(A[i-1])
        str1[1].append('-')
        traceBack(i-1,j)
        count += 1
    elif j > 0 and D[j-1][i] + 1 == D[j][i]: # down
        str1[0].append('-')
        str1[1].append(B[j-1])
        traceBack(i,j-1)
        count += 1
    else: # diagonal
        str1[0].append(A[i-1])
        str1[1].append(B[j-1])
        traceBack(i-1,j-1)
        if A[i-1] != B[j-1]:
            count += 1


count = 0
A = input()
B = input()
traceBack(len(A),len(B))
str1 = [[],[]]
#A = 'BREAD'
#B = 'REALLY'
#str1 = ''
#str2 = ''
#str = [[],[]]
#for i in range(1,len(str[0])+1):
#    str1 += str[0][-i]
#for i in range(1,len(str[1])+1):
#    str2 += str[1][-i]
#print(str1)
#print(str2)
if __name__ == "__main__":
    print(count)
