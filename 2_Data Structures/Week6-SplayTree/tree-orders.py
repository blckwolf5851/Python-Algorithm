# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

    #test
    #self.n = 5
    #self.key = [4,2,5,1,3]
    #self.left = [1,3,-1,-1,-1]
    #self.right = [2,4,-1,-1,-1]

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def recursive(R):
        if self.left[R] != -1:
            recursive(self.left[R])
        self.result.append(self.key[R])
        if self.right[R]!= -1:
            recursive(self.right[R])
    recursive(0)
    return self.result

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def recursive(R):
        self.result.append(self.key[R])
        if self.left[R] != -1:
            recursive(self.left[R])
        if self.right[R]!= -1:
            recursive(self.right[R])
    recursive(0)            
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def recursive(R):
        if self.left[R] != -1:
            recursive(self.left[R])
        if self.right[R]!= -1:
            recursive(self.right[R])
        self.result.append(self.key[R])
    recursive(0)            
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
