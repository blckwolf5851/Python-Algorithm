#Uses python3

import sys
import queue
import math

def distance(adj, s, t):
    #write your code here
    distant[s-1] = 0
    queue=[s]
    for i in adj[s-1]:
        queue.insert(0, i)
    while queue:
        v= queue.pop()
        for m in adj[v-1]:
            if distant[m-1] == -1:
                queue.insert(0,i)
                distant[m-1] = distant[v-1] + 1
    if distant[t-1] != -1:
        return distant[t-1]
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    distant=[-1 for _ in range(n)]
    prev = [i+1 for i in range(n)]
    s, t = data[2 * m], data[2 * m + 1]
    for (a, b) in edges:
        adj[a - 1].append(b)
        adj[b - 1].append(a)
    print(distance(adj, s, t))


#n,m = 4,4
#edges = [[1,2],[4,1],[2,3],[3,1]]
#s,t =2,4
#adj = [[] for _ in range(n)]
#distant=[-1 for _ in range(n)]
#prev = [i+1 for i in range(n)]
#for (a, b) in edges:
#    adj[a - 1].append(b)
#    adj[b - 1].append(a)
#print(distance(adj, s, t))
#print(distant)
#print(prev)