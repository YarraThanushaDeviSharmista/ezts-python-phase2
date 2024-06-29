#bst implementation
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Trees:
    def __init__(self):
        self.root=None
    def insert(self,data):
        newnode=Node(data)
        if self.root==None:
            self.root=newnode
        else:
            curr=self.root
            while True:
                if curr.data<=data:
                    if curr.right==None:
                        curr.right=newnode
                        break
                    else:
                        curr=curr.right
                else:
                    if curr.left==None:
                        curr.left=newnode
                        break
                    else:
                        curr=curr.left
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    def searchnode(self,data):
        s=self.search(self.root,data)
        if s!=None:
            print("found")
        else:
            print("not found")
    def search(self,root,data):
        if root==None or root.data==data:
            return root
        else:
            return self.search(root.left,data) or self.search(root.right,data)        
t=Trees()
t.insert(5)
t.insert(3)
t.insert(4)
t.insert(7)
t.insert(6)
t.inorder(t.root)
t.searchnode(4)

