class ListNode:
  def __init__(self, value):
    self.val = value
    self.next = None

class MyStack:
  def __init__(self):
    self.top = None

  def push(self, value):
    new = ListNode(value)
    new.next = self.top
    self.top = new

  def pop(self):
    if self.top:
      cur = self.top
      self.top = self.top.next
      return cur.val
    else:
      return float('inf')

  def peek(self):
    if self.top:
      return self.top.val
    else:
      return float('inf')

  def isEmpty(self):
    return not self.top

#Test cases
def main():
  myStack = MyStack()
  print("Pushed 2 to stack")
  myStack.push(2)
  print("Top element is %d" %myStack.peek())
  print("Stack is empty: %r" %myStack.isEmpty())
  print("Pushed 5 to stack")
  myStack.push(5)
  print("Top element is %d" %myStack.peek())
  print("Popped element %d" %myStack.pop())
  print("Popped element %d" %myStack.pop())
  print("Top element is %f" %myStack.peek())
  print("Stack is empty: %r" %myStack.isEmpty())
main()
