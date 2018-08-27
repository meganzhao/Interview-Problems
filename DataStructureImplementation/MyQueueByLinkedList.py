class QueueNode:
  def __init__(self, value):
    self.val = value
    self.next = None

class MyQueue:
  def __init__(self):
    self.front = None
    self.rear = None

  def enqueue(self, value):
    newNode = QueueNode(value)
    if self.rear:
      self.rear.next = newNode
    self.rear = newNode
    if not self.front:
      self.front = newNode

  def dequeue(self):
    if not self.front:
      return float('inf')
    if self.front == self.rear:
      self.rear = None
    cur = self.front
    self.front = self.front.next
    return cur.val

  def front(self):
    if self.front:
      return self.front.val
    else:
      return float('inf')

  def rear(self):
    if self.rear:
      return self.rear.val
    else:
      return float('inf')

  def isEmpty(self):
    return self.front == self.rear == None


#Test cases
def main():
  myQueue = MyQueue()
  print("Enqueued 2 to queue")
  myQueue.enqueue(2)
  print("Rear element is %d" %myQueue.rear())
  print("Front element is %d" %myQueue.front())
  print("Queue is empty: %r" %myQueue.isEmpty())
  print("Enqueued 5 to queue")
  myQueue.enqueued(5)
  print("Rear element is %d" %myQueue.peek())
  print("Dequeued element %d" %myQueue.pop())
  print("Dequeued element %d" %myQueue.pop())
  print("Front element is %f" %myQueue.peek())
  print("Queue is empty: %r" %myQueue.isEmpty())
main()
