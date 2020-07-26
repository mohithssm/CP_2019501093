class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        if self.root and isinstance(find_val, int):
            return self.preorder_search(self.root, find_val)
        else:
            return False        

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        self.preorder_print(self.root)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal.append(start.value)
            if start.left:
                self.preorder_print(self.left, traversal)
            # if start.right:
            #     self.preorder_print(self.right, traversal)