class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next

class Dll:
    def __init__(self,start=None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        n = Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n    
    def insert_at_last(self,data):
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
        n = Node(temp,data,None)  
        if temp is None:
            self.start = n
        else:
            temp.next = n

    def search_(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
            
        return None    
    def insert_after(self,temp,data): 
        if temp is not None:
            n = Node(temp,data,temp.next)
            if temp.next is not None:
             temp.next.prev = n
            temp.next = n
    def print_all(self):
        temp = self.start
        while temp is not None:
         print(temp.item,end=" ")
         temp = temp.next
            
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
              self.start.prev = None  
    def delete_last(self):
        temp = self.start
        if self.start == None:
            pass
        elif self.start.next is None:
            self.start = None
            # self.start.prev = None
        else:
            if temp.next.next is not None:
                while temp.next is not None:
                    temp = temp.next
                temp.prev.next = None   
    def delete_item(self,data):
             temp = self.start
             while temp is not None:
                 if temp.item == data:
                      if temp.next is not None:
                           temp.next.prev = temp.prev
                      if temp.prev is not None:
                           temp.prev.next = temp.next
                      else:
                           self.start = temp.next
                      break   
                 temp = temp.next

    def __iter__(self):
        return Dll_iterator(self.start)
    
class Dll_iterator:
    def  __init__(self,start):
       self.current = start
    def __iter__(self):
      return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

my_list = Dll()
my_list.insert_at_start(5)
my_list.insert_at_start(4)
my_list.insert_at_start(3)
my_list.insert_at_start(2)
my_list.insert_at_start(1)
my_list.insert_at_last(7)
my_list.insert_at_last(8)
my_list.insert_after(my_list.search_(5),6)
my_list.search_(7)

my_list.print_all()
my_list.delete_first()
my_list.delete_last()
my_list.delete_item(4)
print()
for x in my_list:
    print(x,end=" ")