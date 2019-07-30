class node:
    def __init__(self,data):
        self.data=data
        self.child=[]
    def insert(self,p,dat):
        d=[]
        if p==self.data:
            self.child.append(node(dat))
            return
        else:
            d.extend(self.child)
            while len(d)>0:
                s=d[0]
                if p==s.data:
                    s.child.append(node(dat))
                    return
                else:
                    if s.child:
                         d.extend(s.child)
                del d[0]
                        
def bfs(nn):
    if nn:
        ss=nn and [nn]
        while len(ss)>0:
            print(ss[0].data)
            if ss[0].child:
                ss.extend(ss[0].child)
            del ss[0]
            
        
        
            
        
na=node(5)
na.insert(5,3)
na.insert(5,6)
na.insert(5,7)
na.insert(6,8)
na.insert(6,88)
bfs(na)





                    
