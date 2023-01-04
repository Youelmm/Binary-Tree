class BinaryTree():
    
    def __init__(self, root=None):
        self.root = root

    def contains(self, node) -> bool:
        current_node = self.root
        while True:
            if current_node == None:
                return False
            elif current_node == node:
                return True
            elif current_node < node:
                current_node = current_node.right_node
            else:
                current_node = current_node.left_node
                
    def insert(self, node):
        previous_node = None
        current_node = self.root
        is_left = None
        while True:
            if node < current_node:
                is_left = True
                previous_node = current_node
                current_node = current_node.left_node
            elif node > current_node:
                is_left = False
                previous_node = current_node
                current_node = current_node.right_node
            elif current_node == None:
                if is_left:
                    previous_node.left_node = node
                elif not is_left:
                    previous_node.right_node = node
                return
            else:
                return
    
    def get_nodes(self):
        nodes_to_handle = []
        current_node = self.root
        nodes_to_handle.append(current_node)
        while len(nodes_to_handle) != 0:
            print(f"{current_node.left_node} <-- {current_node} --> {current_node.right_node}")
            if current_node.left_node != None:
                nodes_to_handle.append(current_node.left_node)
            if current_node.right_node != None:
                nodes_to_handle.append(current_node.right_node)
            nodes_to_handle.pop(0)
            if len(nodes_to_handle) != 0:
                current_node = nodes_to_handle[0]