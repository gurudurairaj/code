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
                    #print(self.data)
    
                else:
                    self.left.insert(data)
            
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                
                else:
                    self.right.insert(data)

        else:
            self.data = data
def su(root,a,ma,ll):
    if root:
        a=a+root.data
        ma=max(a,ma)
        ll.append(ma)
        
        su(root.left,a,ma,ll)
        su(root.right,a,ma,ll)
    return ll
            



    

root = Node(2)
root.insert(1)
root.insert(3)
#root.insert(1)
#root.insert(5)
l=[]
print(max(su(root,0,0,l)))


