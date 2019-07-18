class node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
    def insert(self,p,data):
        if self.data:
            if p==self.data:
                if self.left is None:
                    self.left=node(data)
                else:
                    self.right=node(data)
            else:
                if self.left:
                    self.left.insert(p,data)
                if self.right:
                    self.right.insert(p,data)  
               
def printt(n):
    if n:
        print(n.data)
        printt(n.left)
        printt(n.right)
 
n=node(7)
n.insert(7,5)
n.insert(7,9)
n.insert(5,4)
printt(n)
