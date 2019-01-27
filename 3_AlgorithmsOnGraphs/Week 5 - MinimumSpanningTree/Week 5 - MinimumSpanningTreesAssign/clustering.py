#Uses python3
import sys
import math

def weight(i,j,xy):
    return ((xy[i][0]-xy[j][0])**2 + (xy[i][1] - xy[j][1])**2)**0.5

def find(i,parent,xy): # OK
    if i != parent[i]:  # input a index num
        parent[i] = find(parent[i],parent,xy)
    return parent[i]  #return the root of the given node in index form uses xy[i]

def union(u,v,parent,xy):
    tree1 = find(u,parent,xy) # find xy[u]'s tree root index in xy
    tree2 = find(v,parent,xy) # find b's tree root
    #print(xy[tree1],xy[tree2])
    if tree1 != tree2:
        parent[tree2] = tree1
        



def clustering(x, y, k):
    #write your code here
    xy = [[x[i],y[i],i] for i in range(len(x))]
    edges = []
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            edges.append((i,j,weight(i,j,xy)))
    parent = [i for i in range(len(x))]
    edges = sorted(edges, key=lambda x: x[2])
    uninum=0
    for i in range(len(edges)):
        if find(edges[i][0],parent,xy) != find(edges[i][1],parent,xy):
            uninum+=1
            union(edges[i][0],edges[i][1],parent,xy)
        if uninum > len(x)-k: # n-k = maximum node in first partition, so that the next few group only have one node per each
            return edges[i][2]
    return -1.


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))

#n=4
#x = [0,0,1,1]
#y=[0,1,0,1]
#k = 3
#print("{0:.9f}".format(clustering(x, y, k)))
