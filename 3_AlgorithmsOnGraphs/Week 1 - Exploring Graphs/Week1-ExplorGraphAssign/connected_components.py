#Uses python3

import sys
#def preOrder(x):
#    pre[x] = clock
#    clock += 1

#def postOrder(x):
#    post[x] = clock
#    clock += 1

def explore(adj,x):
    rea[x] = True
    #preOrder(x)
    for w in adj[x]:
        if rea[w] == False:
            explore(adj,w)
    #postOrder(x)

def number_of_components(adj):
    #clock = 1
    #pre = [0 for _ in range(n)]
    #post = [0 for _ in range(n)]
    result = 0
    #write your code here
    for i in range(len(adj)):
        if rea[i] == False:
            explore(adj,i)
            result += 1 
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    rea = [False for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    
    print(number_of_components(adj))
