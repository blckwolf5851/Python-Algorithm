# python3
import sys

def BWT(text):
    bwt = [text]
    result = ""
    for i in range(len(text)-1):
        bwt.append(bwt[-1][-1]+bwt[-1][0:-1])
    bwt.sort()
    for i in bwt:
        result += i[-1]
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
#text = "AACGATAGCGGTAGA$"
#print(BWT(text))