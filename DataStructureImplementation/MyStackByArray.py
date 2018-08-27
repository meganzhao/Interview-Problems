class MyStack:
  def __init__(self):
    self.stack = []
  
  def push(self, value):
    self.stack.append(value)

  def pop(self):
    if len(self.stack) == 0:
      return float('inf')
    else:
      return self.stack.pop()

  def peek(self):
    if len(self.stack) == 0:
      return float('inf')
    else:
      return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

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
