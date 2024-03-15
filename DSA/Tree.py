'''Non linear DSA'''
'''Binary search tree  //Duplicate values not allowed // left values less than right values
    50
  10  70
5 20 60 80
preorder travsing = 50 10 5 20 70 60 80
Inorder trasing gives sorted form 5 10 20 50 60 70 80
post order = 5 20 10 60 80 70 50 '''
class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item = item
        self.left = left
        self.right = right     
class BST:
    def __init__(self):
       self.root = None
    def insert(self,data):
        self.root = self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data<root.item:
            root.left = self.rinsert(root.left,data)    
        elif data>root.item:
            root.right = self.rinsert(root.right,data)
        return root    
    def search(self,data):
        return self.rsearch(self.root,data) 
    def rsearch(self,root,data):
        if root is None or root.item == data:
            return root
        if data<root.item:
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)
    def inorder(self):
        result = []
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
            return
    def preorder(self):
        result = []
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
    def postorder(self):
        result = []
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)   
            result.append(root.item)
    def min_value(self,temp):
        current = temp
        while current.left:
            current = current.left
        return current.item
    def max_value(self,temp):
        current = temp
        while current.right:
            current = current.right
        return current.item    
    def delete(self,data):
        self.root = self.rdelete(self.root,data)
    def rdelete(self,root,data):
        if root is None:
            return root
        if data<root.item:
            root.left = self.rdelete(root.left,data)
        elif data>root.item:
            root.right = self.rdelete(root.right,data)
        else:
            if root.left is None:
               return root.right
            elif root.right is None:
                return root.left
            root.item = self.min_value(root.right)
            self.rdelete(root.right,root.item)
        return root   
    def size(self):
        return len(self.inorder())



bst = BST()
bst.insert(50)
bst.insert(10)
bst.insert(70)
bst.insert(5)
bst.insert(20)
bst.insert(60)
bst.insert(80)
print(bst.inorder())
bst.delete(50)
print(bst.inorder())
# print(bst.max_value())