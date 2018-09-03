class Heap:
  def __init__(self, arr = []):
    if len(arr) == 0:
      self.CAPACITY = 10
      self.array = [0] * self.CAPACITY
      self.size = 0
    else:
      self.CAPACITY = len(arr)
      self.array = [0] * self.CAPACITY
      for i in range(len(arr)):
        self.array[i] = arr[i]
      self.size = len(self.array)
      self.heapify()

  def push(self, element):
    if self.size == self.CAPACITY:
      self.expand()
    self.array[self.size] = element
    self.percolateUp(self.size)
    self.size += 1

  def pop(self):
    if self.size == 0:
      return None
    topValue = self.array[0]
    self.array[0] = self.array[self.size-1]
    self.size -= 1
    self.percolateDown(0)
    return topValue

  def peak(self):
    if self.size > 0:
      return self.array[0]
    else:
      return None

  def update(self, index, value):
    oldValue = self.array[index]
    self.array[index] = value
    if value > oldValue:
      self.percolateDown(index)
    elif value < oldValue:
      self.percolateUp(index)
    return oldValue

  def heapify(self):
    for i in range(self.size//2-1, -1, -1):
      self.percolateDown(i)

  def length(self):
    return self.size

  def isEmpty(self):
    return self.size == 0
    
  def percolateDown(self, index):
    while (index * 2 + 1 < self.size):
      smallerIndex = index * 2 + 1 
      rightIndex = index * 2 + 2
      if rightIndex < self.size and self.array[rightIndex] < self.array[smallerIndex]:
        smallerIndex = rightIndex
      if self.array[index] > self.array[smallerIndex]:
        self.array[smallerIndex], self.array[index] = self.array[index], self.array[smallerIndex]
        index = smallerIndex
      else:
        break
 
  def percolateUp(self, index):
    while index != 0:
      parent = (index - 1) // 2
      if self.array[index] < self.array[parent]:
        self.array[index], self.array[parent] = self.array[parent], self.array[index]
      else:
        break
      index = parent  

  def expand(self):
    self.CAPACITY = int(1.5 * self.CAPACITY)
    tempArr = [0] * self.CAPACITY
    for i in range(self.size):
      tempArr[i] = self.array[i]
    self.array = tempArr

  def __str__(self):
    return str(self.array[:self.size])

def main():
  heap = Heap()
  heap.push(1)
  print(heap)
  heap.push(100)
  heap.push(40)
  heap.push(20)
  print(heap) 
  heap.update(3, 2)
  print(heap)
  heap.pop()
  print(heap)

  newHeap = Heap([4,2,90,6,3,2])
  print(newHeap)

main()        
