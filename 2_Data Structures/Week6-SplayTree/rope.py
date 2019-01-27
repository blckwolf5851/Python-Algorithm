# python3
import sys

class Rope:
  def __init__(self, s):
    self.s = s
  def result(self):
    return self.s
  def process(self, i, j, k):
    words = self.s
    cut = words[i:j + 1]
    need1 = words[:i]
    need2 = words[j + 1:]
    words = need1 + need2
    insert1 = words[:k]
    insert2 = words[k:]
    self.s = insert1 + cut + insert2
                
rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(int(i), int(j), k)
print(rope.result())
