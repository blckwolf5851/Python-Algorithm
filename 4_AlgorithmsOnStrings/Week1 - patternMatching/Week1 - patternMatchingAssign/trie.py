#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}} level by level: A & T in the first level
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    tree[0] = {}    
    # write your code here
    num = 1 # num always indicates the next level
    for i in patterns:
        curNode = 0 # indicates the checking level
        for j in range(len(i)):
            if i[j] not in tree[curNode]: # if the letter in pattern not in the current level
                tree[curNode][i[j]] = num # creat3 a new node that's mark with the node number
                if not j == len(i) -1:
                    tree[num] = {} # preparing for next level
                num+=1 # update node number
            curNode = tree[curNode][i[j]] # update curNode to next level
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))

#patterns =  ["AT","AG","AC"]
#tree = build_trie(patterns)
#for node in tree:
#    for c in tree[node]:
#        print("{}->{}:{}".format(node, tree[node][c], c))
