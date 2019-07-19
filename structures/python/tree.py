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

    def set_root(self, value):
        self.root = value
        return value

    def compare(self, node, new_node):
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    def insert(self, new_value):
        node = self.get_root()
        new_node = Node(new_value)
        if node == None:
            self.set_root(new_node)
            return new_node
        while True:
            comparison = self.compare(node, new_node)
            if comparison == 0:
                return new_node
            elif comparison == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    return new_node
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    return new_node
              
    def search(self, value):
        node = self.get_root()
        test_node = Node(value)
        if node == None:
            return False        
        while True:
            comparison = self.compare(node, test_node)
            if comparison == 0:
                return True
            elif comparison == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    return False
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False            
        return

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        string = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                string += " | " + str(node) 
            else:
                string += "\n" + str(node)
                previous_level = level            
        return string

    def pre_order(self):
        visit_order = list()
        root = self.get_root()
        def traverse(node):
            if node:
                visit_order.append(node.get_value())
                traverse(node.get_left_child())
                traverse(node.get_right_child()) 
        traverse(root)
        return visit_order

    def in_order(self):
        visit_order = list()
        root = self.get_root()

        def traverse(node):
            if node:
                traverse(node.get_left_child())
                visit_order.append(node.get_value())
                traverse(node.get_right_child()) 

        traverse(root)
        return visit_order

    def post_order(self):
        visit_order = list()
        root = self.get_root()

        def traverse(node):
            if node:
                traverse(node.get_left_child())
                traverse(node.get_right_child()) 
                visit_order.append(node.get_value())
        traverse(root)
        return visit_order

    def bfs(self):
        visit_order = list()
        q = Queue()
        node = self.get_root()
        q.enq(node)
        while len(q) > 0:
            node = q.deq()
            visit_order.append(node)
            if node.has_left_child():
                q.enq(node.get_left_child())
            if node.has_right_child():
                q.enq(node.get_right_child())
        return visit_order