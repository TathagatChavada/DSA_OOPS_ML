class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.item = value
        
    
    def count_Nodes(self, root):
        if (root is None):
            return 0
        
        return (1 + self.count_Nodes(root.left) + self.count_Nodes(root.right))
    
    
    def is_complete(self, root, index, number_of_nodes):
        if (root is None):
            return True
        
        elif (index >= number_of_nodes):
            return False
        
        else:
            return (self.is_complete(root.left, 2 * index + 1, number_of_nodes) and
                    self.is_complete(root.right, 2 * index + 2, number_of_nodes))
    

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)


node_count = root.count_Nodes(root)

if root.is_complete(root, 0, node_count):
    print("The tree is a complete binary tree")
    
else:
    print("The tree is not a complete binary tree")