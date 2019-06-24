from queue import Queue

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def get_val(self):
        return self.value
    
    def set_val(self, value):
        self.value = value
        return self.value
    
    def get_left_child(self):
        return self.left
    
    def set_left_child(self, node):
        self.left = node
        return self.left
    
    def has_left_child(self):
        return self.left is not None
    
    def get_right_child(self):
        return self.right

    def set_right_child(self, node):
        self.right = node
        return self.right

    def has_right_child(self):
        return self.right is not None

class Tree:
    def __init__(self, root=None):
        self.root = root
        
    def get_root(self):
        return self.root

def pre_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            visit_order.append(node.get_value())
            traverse(node.get_left_child())
            traverse(node.get_right_child()) 

    traverse(root)
    return visit_order
def in_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            traverse(node.get_left_child())
            visit_order.append(node.get_value())
            traverse(node.get_right_child()) 

    traverse(root)
    return visit_order

def post_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            traverse(node.get_left_child())
            traverse(node.get_right_child()) 
            visit_order.append(node.get_value())

    traverse(root)
    return visit_order

def bfs(tree):
    visit_order = list()
    q = Queue()
    node = tree.get_root()
    q.enq(node)
    def traverse():
        node = q.deq()
        visit_order.append(node)
        if node.has_left_child():
            q.enq(node.get_left_child())
        if node.has_right_child():
            q.enq(node.get_right_child())
            
    return visit_order