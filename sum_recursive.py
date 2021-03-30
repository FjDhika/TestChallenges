import math

class node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
    def setValue(self,val):
        self.value = val

def transverse(node, sm = 0):
    root = node
    if root.left != None:
        sm = transverse(root.left, sm)
    if root.right != None:
        sm = transverse(root.right, sm)
    return sm + root.value

def insert(val):
    current = node()
    if val > 1:
        current.left = insert(val//2)
        current.right = insert(int(math.sqrt(val)))
    current.setValue(val)
    return current

def sum_recursive(number):
    root = insert(int(number))
    return transverse(root)


