#Uses python3
import sys
import queue


#def shiftDown(i):
#    ind = i
#    l = 2*i
#    r = 2*i+1
#    if l < n and H[l] < H[ind]:
#        ind = l
#    if r < n and H[r] < H[ind]:
#        ind = r
#    if i != ind:
#        H[i],H[ind] = H[ind], H[i]
#        shifrDown(ind)

#def shiftUp(i):
#    parent = i//2
#    if H[parent] > H[i]:
#        H[parent],H[i] = H[i], H[parent]
#        shiftUp[parent]

#def extractMin():
#    min = H[0]
#    H[0] = H[n-1]
#    shiftDown(0)
#    return min

def findMin(H):
    min = (10**4)
    for i in range(len(H)):
        if H[i] != (10**4):
            if H[i][1] < min:
                min = H[i][1]
    for i in range(len(H)):
        if H[i] != (10**4):
            if H[i][1] == min:
                return i

def check(H):
    try:
        s = sum(H)
        if s == (10**4)*n:
            return True
    except:
        return False


    
def distance(adj, s, t):
    #write your code here
    dist = [(10**4) for _ in range(n)]
    H = [[i+1,(10**4)] for i in range(n)]
    prev = [None for _ in range(n)]
    H[s-1][1] = 0
    prev[s-1] = s
    while not check(H):
        ind = findMin(H)
        u = H[ind][0]
        dis = H[ind][1]
        dist[u-1] = dis
        H[ind] = (10**4)
        for v in adj[u-1]:
            if H[v[0]-1] != (10**4):
                if H[v[0]-1][1] > dis + v[1]:
                    H[v[0]-1][1] = dis + v[1]
                    prev[v[0]-1] = u
    if prev[t-1] != None:
        return dist[t-1]
    
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 *
    m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append((b,w))
        #cost[a - 1].append(w)
    s, t = data[0], data[1]
    print(distance(adj, s, t))

#n,m = 10,9
#edges = [((1,2),1),((6,7),1),((8,9),1),((9,10),1),((3,4),1),((7,8),1),((4,5),1),((5,6),1),((2,3),1)]
#adj = [[] for _ in range(n)]
#cost = [[] for _ in range(n)]
#for ((a, b), w) in edges:
#    adj[a - 1].append((b,w))
#s,t = 1,10
#print(distance(adj, s, t))

#heap_builder = Heap()
#heap_builder.ReadData()
#heap_builder.BuildHeap()
#print(heap_builder._data)
