class Node: 
    def __init__(self, key): 
        self.key = key 
        self.child=[]
def createNode(parent, i, created, root): 
  
    if created[i] is not None: 
        return 
    created[i] = Node(i) 
   
    if parent[i] == -1: 
        root.append(created[i])
        return
 
    if created[parent[i]] is None: 
        createNode(parent, parent[i], created, root ) 
  
    p = created[parent[i]]
    p.child.append(created[i])
  
  
  

def createTree(parent): 
    n = len(parent) 
      
    created = [None for i in range(n+1)] 
      
    root = [] 
    for i in range(n): 
        createNode(parent, i, created, root) 
  
    return root
  

def inorder(root):
    ss=[]
    for ii in range(len(root)):
        ss.extend(root[ii] and [root[ii]])
    while len(ss)>0:
        print(ss[0].key)
        if ss[0].child:
            ss.extend(ss[0].child)
        del ss[0]
def bfs(root):
    ss=[]
    v=0
    for ii in range(len(root)):
        ss.extend(root[ii] and [root[ii]])
    while len(ss)>0:
        g=len(ss)
        for u in range(g):
             print(ss[0].key,end="")
             if ss[0].child:
                 ss.extend(ss[0].child)
             del ss[0]
        v=v+1
        print()
    print(v)
            
            
        
    
    
        
parent = [1,5,5,2,2,-1,3,-1] 
root = createTree(parent)

inorder(root)
bfs(root)
# 2 -1 4 5 -1
