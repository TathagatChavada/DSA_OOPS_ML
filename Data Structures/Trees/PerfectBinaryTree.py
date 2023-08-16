class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.item = value
        
        
    def calculateDepth(self, node):
        d = 0
        
        while (node is not None):
            d += 1
            node = node.left
        
        return d
    
    
    def is_Perfect(self, root, d, level = 0):
        
        if (root is None):
            return True
        
        elif (root.left is None) and (root.right is None):
            return (d == level + 1)
        
        elif (root.left is None) or (root.right is None):
            return False
        
        else:
            return (self.is_Perfect(root.left, d, level + 1) and 
                    self.is_Perfect(root.right, d, level + 1))
            

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

# root.right.left = Node(6)
# root.right.right = Node(7)


if (root.is_Perfect(root, root.calculateDepth(root))):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")

