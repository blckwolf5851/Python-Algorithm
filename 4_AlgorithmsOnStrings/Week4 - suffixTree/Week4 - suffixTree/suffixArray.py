#uses python3


# Initialization

def initialCS(S):
    global alpha
    order = [0 for _ in range(len(S))]
    count = [[i,0] for i in range(128)]
    for i in S:
        count[ord(i)][1] += 1
    for j in range(1,len(count)):
        count[j][1] += count[j-1][1]
    alpha = count
    #print(count[ord("$")] + count[ord("a")] + count[ord("b")])
    i = len(S)-1
    while i >= 0:
        char = S[i]
        count[ord(char)][1] -= 1
        order[count[ord(char)][1]] = i
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
        curSecond = newOrder[i] + L
        prevFirst = newOrder[i-1]
        prevSecond = newOrder[i-1] + L
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
        order = sortDouble(S,order,clas,1)
        clas = updateClass(order, clas, 1)
        L *= 2
    return order
        
def search(S,P, order,alpha):
    #count = [[i,0] for i in range(128)]
    #for i in S:
    #    count[ord(i)][1] += 1
    #alphaLen = count #[count[i] for i in range(len(count))]
    ##print(alphaLen[ord("b")])
    #min = alphaLen[ord(P[0][0])][1]
    #for j in range(1,len(count)):
    #    count[j][1] += count[j-1][1]
    #print("***********",alphaLen[ord(P[0][0])])
    #max = count[ord(P[0])][1]
    
    #print(max,min)

    min = alpha[ord(P[0])][1]
    result = ""
    n = len(P)
    for i in range(min, len(order)):
        if S[order[i]:order[i]+n] == P:
            result += str(order[i]) + " "
        elif S[order[i]] != P[0]:
            break
    return result

def assign(S, P):
    result = ""
    
    for i in P:
        ind = search(S,i,order,alpha)
        result += ind
    #print("result", result)
    return result

S = "atatata$"
P = ["ata","c", "tatat"]
alpha = None
order = buildSuffix(S)
print(assign(S,P))

