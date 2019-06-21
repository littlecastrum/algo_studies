class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
  
  def __repr__(self):
    return str(self.value)

class LinkedList:
  def __init__(self, init_list=None):
    self.head = None
    self.tail = None
    self.num_nodes = 0
    if init_list:
      self.from_list(init_list)

  def __iter__(self):
    node = self.head
    while node:
      yield node.value
      node = node.next
          
  def __repr__(self):
    return str([v for v in self])
  
  def flatten(self):
    return self._flatten(self.head)

  def prepend(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = self.head
    else:
      new_node.next = self.head
      self.head = new_node
    self.num_nodes += 1
    return self.head
      
  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = self.head
    else:
      self.tail.next = new_node
      self.tail = self.tail.next
    self.num_nodes += 1
    return self.head

  def search(self, value):
    node = self.head
    target = None
    while target is None:
      if node.value == value:
        target = node
      elif node is None:
        target = None
      else:
        node = node.next
    return target

  def remove(self, value):
    if self.is_empty() is False:
      if self.head.value == value:
        self.head = self.head.next
        self.num_nodes -= 1
      else:
        anchor = self.head
        runner = self.head.next
        while runner.value != value or runner is None:
          anchor = runner
          runner = runner.next
        if runner is not None:
          if runner.next == None:
            self.tail = anchor
            self.tail.next = None
          else:
            anchor.next = runner.next
          self.num_nodes -= 1
    return self.head

  def pop(self):
    target = self.head.value
    self.head = self.head.next
    self.num_nodes -= 1
    return target
  
  def insert(self, value, pos):
    if pos == 0:
      self.prepend(value)
    elif pos >= self.size():
      self.append(value)
    else:
      counter = 0
      new_node = Node(value)
      left_node = self.head
      while counter != (pos - 1):
        counter += 1
        left_node = left_node.next
      right_node = left_node.next
      left_node.next = new_node
      new_node.next = right_node
      self.num_nodes += 1
    return self.head

  def is_empty(self):
    return self.size == 0

  def size(self):
    return self.num_nodes

  def read_list(self):
    head = self.head
    while head:
      print(head.value)
      head = head.next
    return self.head

  def from_list(self, arr):
    for value in arr:
      self.append(value)

  def reverse(self):
    reverse_list = LinkedList()      
    node = self.head
    while node:
      reverse_list.prepend(node.value)
      node = node.next
    return reverse_list
  
  def iscircular(self):
    slow = self.head
    if slow is not None:
      fast = slow.next
      while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

  def _flatten(self, node):
    if node.next is None:
      return merge(node.value, None)
    return merge(node.value, self._flatten(node.next))

def merge(list1, list2):
  merged = LinkedList(None)
  if list1 is None:
    return list2
  if list2 is None:
    return list1
  list1_elt = list1.head
  list2_elt = list2.head
  while list1_elt is not None or list2_elt is not None:
    if list1_elt is None:
      merged.append(list2_elt)
      list2_elt = list2_elt.next
    elif list2_elt is None:
      merged.append(list1_elt)
      list1_elt = list1_elt.next
    elif list1_elt.value <= list2_elt.value:
      merged.append(list1_elt)
      list1_elt = list1_elt.next
    else:
      merged.append(list2_elt)
      list2_elt = list2_elt.next
  return merged

def make_ll_even_after_odd(node):
  even = None
  odd = None
  while node:
    if node.data % 2 == 0:
      if even is None:
        even = node
      else:
        even.next = node
        even = node
    else:
      if odd is None:
        odd = node
      else:
        odd.next = node
        odd = node
    node = node.next

def skip_i_delete_j(head, i, j):
  if i == 0:
    return None
  if head is None or j < 0 or i < 0:
    return head
  counter = 0
  runner = head
  anchor = None
  while runner:
    counter += 1
    if counter == 3:
      anchor = head
    if counter == 6:
      anchor.next = next
      counter = 0
    runner = runner.next

def swap_nodes(head, left, right):
  anchor = None
  node = head
  for position in range(left):
    if position == (left - 1):
      anchor = head
    node = node.next
      
  right_anchor = node.next.next
  anchor.next = node.next
  anchor.next.next = node
  anchor.next.next.next = right_anchor
