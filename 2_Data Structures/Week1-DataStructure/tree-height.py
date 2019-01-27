#uses python 3
#def rec(a,l,r):
#    if l+1 == r:
#        return 2
#    mid = (l+r)//2
#    L=rec(a,l,mid)
#    R=rec(a,mid,r)
#    return max(L,R)+1
#
#n = input()
#inp = input()
#a = [int(n) for n in inp.split()]

#print(rec(a,0,len(a))-1)

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size

class TreeHeight:

    def __init__(self):
        self.n = 0
        self.parent = []
        self.cache = []

    def read(self):
        """Reads input."""
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.cache = [0] * self.n

    def path_len(self, node_id):
        """Returns path length """
        parent = self.parent[node_id]
        if parent == -1:
            return 1

        if self.cache[node_id]:
            return self.cache[node_id]

        self.cache[node_id] = 1 + self.path_len(self.parent[node_id])
        return self.cache[node_id]

    def compute_height(self):
        """mac tree height."""
        return max([self.path_len(i) for i in range(self.n)])


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()