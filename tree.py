class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
    
                else:
                    self.left.insert(data)
            
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                
                else:
                    self.right.insert(data)

        else:
            self.data = data

def ino(root):
    if root:
       
        sd=ino(root.left)
        print(root.data)
        sdd=ino(root.right)

    

root = Node(6)
root.insert(4)
root.insert(8)
root.insert(1)
root.insert(5)
ino(root)

