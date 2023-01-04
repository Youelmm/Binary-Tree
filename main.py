from binarytree import BinaryTree
from node import Node
from random import randint
from time import time

class Benchmark:
    
    def __init__(self, binary_tree):
        self.binary_tree = binary_tree
    
    def launch(self, nodes_to_find: list[Node]):
        start = time()
        for node in nodes_to_find:
            if self.binary_tree.contains(node):
                print(f"{node} is present")
            else:
                print(f"{node} is not present")
        end = time()
        average_time = (end - start) / len(nodes_to_find)
        print(f"Average time: {average_time} ns")


if __name__ == "__main__":
    node = Node(23)
    binary_tree = BinaryTree(node)
    binary_tree.insert(node)
    # Insert some nodes
    for i in range(20):
        node = Node(randint(-100, 100))
        binary_tree.insert(node)
    # Create a benchmark object
    benchmark = Benchmark(binary_tree)
    benchmark.launch([Node(randint(-100, 100)) for i in range(30)])