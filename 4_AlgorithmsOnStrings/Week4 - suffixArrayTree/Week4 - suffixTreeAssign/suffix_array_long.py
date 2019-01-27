# python3
import sys


# Initialization

def initialCS(S):
    order = [0 for _ in range(len(S))]
    count = [0 for i in range(128)]
    for i in S:
        count[ord(i)] += 1
    for j in range(1,len(count)):
        count[j] += count[j-1]
    #print(count[ord("$")] + count[ord("a")] + count[ord("b")])
    i = len(S)-1
    while i >= 0:
        char = S[i]
        count[ord(char)] -= 1
        order[count[ord(char)]] = i
        i-=1
    return order

def equivClass(S,order):
    clas = [0 for _ in range(len(S))]
    clas[order[0]] = 0
    for i in range(1,len(order)):
        if S[order[i]] != S[order[i-1]]:
            clas[order[i]] = clas[order[i-1]] + 1
        else:
            clas[order[i]] = clas[order[i-1]]
    return clas

# Update
def sortDouble(S,order,clas,L):
    count = [0 for _ in range(len(S))]
    newOrder = [0 for _ in range(len(S))]
    for i in clas:
        count[i] += 1
    for j in range(1, len(count)):
        count[j] += count[j-1]
    i = len(S)-1
    while i >= 0:
        char = (order[i]-L + len(S)) % len(S)
        cl = clas[char]
        count[cl] -= 1
        newOrder[count[cl]] = char
        i-=1
    return newOrder

def updateClass(newOrder,clas,L):
    n = len(newOrder)
    newClass = [0 for _ in range(n)]
    newClass[newOrder[0]] = 0
    for i in range(1,n):
        curFirst = newOrder[i]
        curSecond = (curFirst + L) % n
        prevFirst = newOrder[i-1]
        prevSecond = (prevFirst + L) % n
        if clas[curFirst] != clas[prevFirst] or clas[curSecond] != clas[prevSecond]:
            newClass[curFirst] = newClass[prevFirst] + 1
        else:
            newClass[curFirst] = newClass[prevFirst]
    return newClass

# Build
def buildSuffix(S):
    order = initialCS(S)
    clas = equivClass(S, order)
    L = 1
    while L < len(S):
        order = sortDouble(S,order,clas,L)
        clas = updateClass(order, clas, L)
        L *= 2
    return order

#S = "AACGATAGCGGTAGA$"
#print(" ".join(map(str, buildSuffix(S))))
if __name__ == '__main__':
  S = sys.stdin.readline().strip()
  print(" ".join(map(str, buildSuffix(S))))
