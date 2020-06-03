

class Heap(object):
    def __init__(self):
        self.heap = [0]
        self.currentSize = 0

    def __str__(self):
        heap = self.heap[1:]
        return ' '.join(str(i) for i in heap)

    def Up(self, index):
        while (index // 2) > 0:
            if self.heap[index] < self.heap[index // 2]:
                temp = self.heap[index // 2]
                self.heap[index // 2] = self.heap[index]
                self.heap[index] = temp
            index = index // 2

    def insert(self, key):
        self.heap.append(key)
        self.currentSize += 1
        self.Up(self.currentSize)

    def Down(self, index):
        while(index * 2) <= self.currentSize:
            minimumChild = self.minChild(index)
            if self.heap[index] > self.heap[minimumChild]:
                temp = self.heap[index]
                self.heap[index] = self.heap[minimumChild]
                self.heap[minimumChild] = temp
            index = minimumChild

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heap[i * 2] < self.heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delete(self):
        deletedNode = self.heap[1]
        self.heap[1] = self.heap[self.currentSize]
        self.currentSize -= 1
        self.heap.pop()
        self.Down(1)
        return deletedNode

    def build(self, tab):
        i = len(tab) // 2
        self.currentSize = len(tab)
        self.heap = [0] + tab[:]
        while (i > 0):
            self.Down(i)
            i = i - 1

bh = Heap()
bh.build([11,5,8,0,3,5])

print('Del:', bh.delete())
print('Del:', bh.delete())
print('Del:', bh.delete())
bh.insert(3)
print('Del:', bh.delete())
print(bh)
