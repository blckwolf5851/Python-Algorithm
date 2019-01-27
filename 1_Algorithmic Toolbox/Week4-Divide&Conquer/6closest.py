#Uses python3
import sys
from operator import attrgetter
from collections import namedtuple

Cords = namedtuple('Cords', 'start end')

# calculate distance
def dist(p1,p2):
    return ((p2[0]-p1[0]) ** 2 + (p2[1]-p1[1]) ** 2) ** 0.5

# minimum distance between 3 points
def bruteforce(p):
    minDis = 10000000
    for i in range(len(p)):
        for j in  range(i+1,len(p)): 
            if dist(p[i],p[j]) < minDis:
                minDis = dist(p[i],p[j])
    return minDis
# minimum number between 2
def min (v1,v2):
    if float(v1) >= float(v2):
        return float(v2)
    else:
        return float(v1)

# find minimum distance amoung midplane
def midplain(p,d):
    min = d
    i = 0
    j = i + 1
    p = sorted(p, key = lambda x: x[ 1 ])
    for i in range(len(p) - 1):
        if p[i+1][1]-p[i][1] < min:
            for j in range(i + 1, len(p)):
                if dist(p[j],p[i]) < min:
                    min = dist(p[j],p[i])
    return min


def minimum_distance(cords, l, r):
    # base case
    if r-l <= 3:
        return bruteforce(cords[l:r])

    # sort by x
    cords.sort()
    # divide cordinates by half recursively
    mid = (l+r-1) // 2
    midInd = cords[mid+1]
    pl = minimum_distance(cords,l, mid+1)
    pr = minimum_distance(cords, mid+1,r)
    # find minimum value amoung two distance
    d = min(pl,pr)
    # append middle part amoung the vertical line that cut cords in half
    midpart = []
    # fine minimum distance between midplane
    for i in range(l,r):
        if abs(abs(cords[i][0])-abs(midInd[0]))< d:
            midpart.append(cords[i])
    midmini = midplain(midpart,d)
    dis = min(midmini,d)
    return dis

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    cords = list(map(lambda x: Cords(x[0], x[1]), zip(data[::2], data[1::2])))
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    #n = data[0]
    #x = data[1::2]
    #y = data[2::2]
#cordtest = [[4,4],[-2,-2],[-3,-4],[2,3],[-1,3],[1,1],[-4,0],[-1,-1],[3,-1],[-4,2],[-2,4]]
#cordtest = [[0,0],[3,4]]
    print(minimum_distance(cords,0,len(cords)))
