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
        

def minimum_distance(x, y):
    result = 0

    xy = [[x[i],y[i],i] for i in range(len(x))]
    edges = []
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            edges.append((i,j,weight(i,j,xy)))
    parent = [i for i in range(len(x))]
    edges = sorted(edges, key=lambda x: x[2])
    #print(xy)
    #print(edges)
    for i in range(len(edges)):
        if find(edges[i][0],parent,xy) != find(edges[i][1],parent,xy):
            #print("xy:",xy)
            #print("parent:",parent)
            #print("edgesUnion:",find(edges[i][0],parent,xy),find(edges[i][1],parent,xy))
            
            #print("weight:",edges[i][2])
            result += edges[i][2]
            #print("union: ", edges[i][0],edges[i][1])
            union(edges[i][0],edges[i][1],parent,xy)
            #print("parent:",parent)
    #print(parent)
    #write your code here
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
#n=4
#x = [0,0,1,1]
#y=[0,1,0,1]
#print("{0:.9f}".format(minimum_distance(x, y)))