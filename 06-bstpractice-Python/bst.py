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
        self.printSelf_helperfunc(self.root)

    def search(self, find_val):
        if self.root and isinstance(find_val, int):
            r = self.search_helperfunc(self.root, find_val)
            return True if r else False
        return False        

    def insert_helperfunc(self, root, new_val):
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
        if root is None:
            return
        else:
            print(" ",root.value)
            self.printSelf_helperfunc(root.left)
            self.printSelf_helperfunc(root.right)

        
    def search_helperfunc(self, root, find_val):
        if root is None or root.value == find_val:
            return root
        if root.value < find_val:
            return self.search_helperfunc(root.right, find_val)
        else:
            return self.search_helperfunc(root.left, find_val)

