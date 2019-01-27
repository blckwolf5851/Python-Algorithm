def posBWT (text):
    bwt = [text]
    result = []

    for i in range(len(text)-1):
        bwt.append(bwt[-1][-1]+bwt[-1][0:-1])
    #j =len(text)-1
    #for i in range(len(text)):
    #    bwt[i] += str(j)
    #    j-=1
    j = len(text)-1
    i = 1
    while j >= 1:
        bwt[i] += str(j)
        j-=1
        i+=1
    bwt[0] += "0"
    bwt.sort()
    for i in bwt:
        result.append(i[len(text):])

    #for i in range(len(text)):
    #    result[i] += str(j)
    #    j-=1
    
    #print(bwt)
    return result


def BWT(text):
    bwt = [text]
    result = []

    for i in range(len(text)-1):
        bwt.append(bwt[-1][-1]+bwt[-1][0:-1])
    bwt.sort()
    #j = len(text)-1
    #i = 1
    #while j >= 1:
    #    bwt[i] += str(j)
    #    j-=1
    #    i+=1
    #bwt[0] += "0"
    for i in bwt:
        result.append(i[0]+i[-1])

    #for i in range(len(text)):
    #    result[i] += str(j)
    #    j-=1
    
    return result

def preprocess(columns):
    # $,A,C,G,T
    #print(columns)
    firstColum = [[],[],[],[],[]]
    lastColum = [[],[],[],[],[]]
    for i in range(len(columns)):
        firstColum[giveACGT(columns[i][0])].append(i)
        lastColum[giveACGT(columns[i][1])].append(i)
    return firstColum,lastColum

def giveACGT(letter):
    if letter == "$":
        return 0
    if letter == "A":
        return 1
    if letter == "C":
        return 2
    if letter == "G":
        return 3
    if letter == "T":
        return 4

def check(bwt,position,pattern, start):
    i = 1
    top = start
    print (top)
    passed = 0
    current = 0
    while i <= len(pattern):
        
        if bwt[top][0] != pattern[-i]:
            return False
        passed+=1
        i += 1
        if passed == len(pattern):
            break
        #if passed == len(pattern):
        #    return current
        current = top
        ind = position[1][giveACGT(bwt[top][1])].index(top)
        top = position[0][giveACGT(bwt[top][1])][ind]
    return top
        

def matching(text,pattern):
    bwt= BWT(text)
    posbwt = posBWT(text)
    position = preprocess(BWT(text))
    print(position)
    print(posbwt)
    print(bwt)

    #$,A,C,G,T
    current = 0
    symbol = pattern[-1]
    #top = position[0][giveACGT(symbol)][0]
    #bottom = position[0][giveACGT(symbol)][-1]
    result = []
    for top in position[0][giveACGT(symbol)]:
        if not check(bwt,position,pattern,top):
            continue
        else:
            print(check(bwt,position,pattern,top))
            result.append(int(posbwt[top])-len(pattern)+1)
        
    return result
    




text = "ATGCGCATATTAGCTA$"
patterns = "TATTA"
print(matching(text,patterns))