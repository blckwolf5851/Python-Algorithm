#Uses python3

import sys
import queue

def bipartite(adj):
    s=1
    #write your code here
    #if there is a circle in the path tree, then it cannot be bipartite
    distant[s-1] = 0
    queue=[s]
    for i in adj[s-1]:
        queue.insert(0, i)
    while len(queue) != 0:
        v= queue.pop()
        for m in adj[v-1]:
            if distant[m-1] == -1:
                
                queue.insert(0,m)
                distant[m-1] = distant[v-1] + 1
            #check if inner connected
            elif distant[m-1] == distant[v-1]:
                return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    distant=[-1 for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b)
        adj[b - 1].append(a)
    print(bipartite(adj))

#n,m = 4,3
#edges = [[1,2],[3,2],[4,3]]
#adj = [[] for _ in range(n)]
#distant=[-1 for _ in range(n)]
#for (a, b) in edges:
#    adj[a - 1].append(b)
#    adj[b - 1].append(a)
#print(bipartite(adj))