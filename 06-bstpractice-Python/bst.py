class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helperfunc(self.root, new_val)

    def printSelf(self):
        # Your code goes here
        pass
        
    def search(self, find_val):
        # Your code goes here
        pass


    def insert_helperfunc(self, new_val):
        if root is None:
            root = Node(new_val)
        else:
            if root.value < new_val:
                if root.right is None:
                    root.right = Node(new_val)
                else:
                    self.insert_helperfunc(root.right, new_val)
            else:
                if root.left is None:
                    root.left = Node(new_val)
                else:
                    self.insert_helperfunc(root.left, new_val)

    def printSelf_helperfunc(self):
        # Your code goes here
        pass
        
    def search_helperfunc(self, find_val):
        # Your code goes here
        pass

