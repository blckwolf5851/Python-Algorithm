# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = {}
		self.isLeaf = False

def solve (text, n, patterns):
	result = []
	root = Node()
	for pattern in patterns:
		currentNode = root
		for i, c in enumerate(pattern):

			if c not in currentNode.next: # if not in level then append the new node
				currentNode.next[c] = Node()
			if i == len(pattern) - 1: # if is at the last letter in the current pattern, then it's a leaf
				currentNode.next[c].isLeaf = True
			else:
				currentNode = currentNode.next[c] # if it is in the level, update the currentNode with the next level
	
	for i in range(len(text)):
		index = i
		currentNode = root
		while index < len(text):
			c = text[index]
			if c not in currentNode.next: break # if it is not the suffix of any pattern, then no result
			currentNode = currentNode.next[c] # if it is the suffix of the patterns, then update current node into next level
			if currentNode.isLeaf: # if the current node is a leaf, then match, append to result
				result.append(i)
				break
			index+=1 # greedy check the next index if the current node is not leaf and the last letter in text is the suffix of the pattern

	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
