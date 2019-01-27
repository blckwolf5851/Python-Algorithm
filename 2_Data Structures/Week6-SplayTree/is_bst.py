#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

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

def IsBinarySearchTree(array):
  # Implement correct algorithm here
  for i in range(len(array)-1):
      if array[i] > array[i+1]:
          return False
  return True

def main():
  tree = TreeOrders()
  tree.read()
  if IsBinarySearchTree(tree.inOrder()):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
