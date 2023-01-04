class Node:
    
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None
    
    def __lt__(self, other):
        if other == None:
            return False
        return self.value < other.value
    
    def __eq__(self, other):
        if other == None:
            return False
        return self.value == other.value

    def __gt__(self, other):
        if other == None:
            return False
        return self.value > other.value
    
    def __str__(self):
        return str(self.value)
        
    def set_left_node(self, node):
        self.left_node = node
        
    def set_right_node(self, node):
        self.left_node = node        