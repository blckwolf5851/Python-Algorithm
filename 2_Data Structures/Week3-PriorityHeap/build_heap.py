# python3

class Heap:
	def __init__(self):
		self._swaps = []
		self._data = []

	def ReadData(self):
		n = int(input())
		self._data = [int(s) for s in input().split()]
		assert n == len(self._data)

	def WriteResponse(self):
		print(len(self._swaps))
		for swap in self._swaps:
		  print(swap[0], swap[1])

	def GenerateSwaps(self):
		for i in range(int((len(self._data)-2)/2), -1, -1):
			s = i
			while True:
				l = 2*s+1
				r = 2*s+2
				if l>len(self._data)-1: break #check if left child exceed data length
				if r>len(self._data)-1:  #if right child exceed data length, check left child
					if self._data[s]>self._data[l]:# if parent greater than child, swap, then break
						self._swaps.append([s,l])
						self._data[s], self._data[l] = self._data[l], self._data[s]
					break
				if self._data[s]<=min(self._data[l],self._data[r]): break #if parent already smaller than child, break
				k = l if self._data[l]<self._data[r] else r # what's left is those child that are smaller than parent
				self._swaps.append([s,k])
				self._data[s], self._data[k] = self._data[k], self._data[s]
				s = k

	def Solve(self):
		self.ReadData()
		self.GenerateSwaps()
		self.WriteResponse()

if __name__ == '__main__':
	heap_builder = Heap()
	heap_builder.Solve()