class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def append(self, value):
    new_node = DoubleNode(value)

    if self.head is None:
      self.head = new_node
      self.tail = self.head
      return self.head

    new_node.previous = self.tail
    self.tail.next = new_node
    self.tail = self.tail.next

    self.size += 1
    return self.head

  def is_empty(self):
    return self.size == 0

  def read_list(self):
    head = self.head
    while head:
      print(head.value)
      head = head.next
    return self.head

  def from_list(self, arr):
    doubly_linked_list = DoublyLinkedList()
    for value in arr:
      doubly_linked_list.append(value)
    return doubly_linked_list
  
  def __iter__(self):
    node = self.head
    while node:
      yield node.value
      node = node.next
        
  def __repr__(self):
    return str([v for v in self])
