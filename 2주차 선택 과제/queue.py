class queue:
  def __init__(self):
    self.arr = []
    self.front = 0
    self.rear = 0

  def push(self, data):
    self.arr.append(data)
    self.rear += 1

  def isEmpty(self):
    if self.rear == self.front:
      return True
    return False

  def pop(self):
    if self.isEmpty():
      return False
    output = self.arr[self.front]
    self.front += 1
    del (self.arr[self.front - 1])
    return output

  def peek(self):
    if self.isEmpty():
      return False
    return self.arr[self.front]
