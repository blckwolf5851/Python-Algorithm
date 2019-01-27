# python3
import sys


def case2 (pattern,s,b,i):
    while b > 0:
        #n+=1
        if pattern[s[b]] == pattern[i+1]:
            return s[s[b]-1] + 1
        else:
            b = s[b]
    return 0

def compBorder(pattern):
    #n = 0
    s = [0 for _ in range(len(pattern))]
    for i in range(len(pattern)-1):
        #case1
        #n+=1
        if pattern[i+1] == pattern[s[i]]:
            s[i+1] = s[i]+1
        #case 2
        else:
            b = s[i]-1
            if b == 0 and pattern[0] == pattern[i+1]:
                s[i+1] = s[0] + 1
                
            else:
                s[i+1] = case2 (pattern,s,b,i)
    #print(n)
    return s

def compBorder2(pattern):
    s = [0 for _ in range(len(pattern))]
    s[0] = 0
    border = 0
    for i in range(1,len(pattern)):
        while border > 0 and pattern[border] != pattern[i]:
            border = s[border-1]
        if pattern[i] == pattern[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s

def matching(text,pattern):
    PT = pattern + "$" + text
    s = compBorder2(PT)
    
    result = []
    for i in range(len(pattern)+1, len(PT)):
        if s[i] == len(pattern):
            result.append(i - 2 * len(pattern))
    return result

#text = "GATATATGCATATACTT"
#pattern = "ATAT"
#print(matching(text,pattern))

if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = matching(text, pattern)
  print(" ".join(map(str, result)))

