#Uses python3

import sys
#def preorder(x):
#    global clock
#    pre[x]=clock
#    clock += 1

#def postorder(x):
#    global clock
#    post[x] = clock
#    clock += 1

def dfs(adj, used, order, x):
    #write your code here
    used[x] = 1
    #preorder(x)
    for i in range(len(adj[x])):
        if not used[adj[x][i]]:
            dfs(adj,used,order,adj[x][i])
    #postorder(x)
    order.append(x)
    


def toposort(adj):
    used = [0] * len(adj)
    order = []
    #write your code here
    for i in range(n):
        if not used[i]:
            dfs(adj, used, order, i)
    order.reverse()
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    pre = [0 for _ in range(n)]
    post = [0 for _ in range(n)]
    clock = 1

    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

