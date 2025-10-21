class Node:
    def __init__(self, root=None, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node()
            self.data = value
            self.left = null
            self.right = null

    # Left -> Root -> Right
    def inorder_traversal(root):
    # Time Complexity O(n) - n number of nodes
    # Auxiliary Space O(h) - h height of tree
        if root is None:
            return

        # Visiting Left Subtree First
        inorder_traversal(node.left)

        # Printing the Node Data
        print(node.data, end=' ')

        # Visiting the Right Subtree
        inorder_traversal(node.right)

    # Root -> Left -> Right
    def preorder_traversal(root):
        # Time Complexity O(1) - if no recursion stack space is considered
        # Auxiliary Space O(h) - h height of tree
        if root is None:
            return

        # Printing the Node Data First
        print(node.data, end=' ')
        
        # Visiting Left Subtree
        preorder_traversal(node.left)

        # Visiting Right Subtree
        preorder_traversal(node.right)


    # Left -> Right -> Root
    def postorder_traversal(root):
        # Time Complexity O(n) - n number of nodes
        # Auxiliary Space O(h) - if no recursion stack space is considered
        if root is None:
            return

        # Visiting Left Subtree
        postorder_traversal(node.left)

        # Visiting Right Subtree
        postorder_traversal(node.right)

        # Printing the Node Data
        print(node.data, end=' ')

        # Used for Tree deletion as we need to delete 
        # subtrees first before deleting root node


    def level_order_traversal(root):
        if root in None:
            return

        
        
        




