# What is list ?
# ans = linear collection of data items
'''example : 23,56,8,9,45,67.. list of marks   (integer type of list)
             indore,jaipur,ahmedabaad,jalore,sirohi.. city names  (string type of list)
             Atul- 100 - 25000, arjun-101-50000, armaan -102-34000 (Employ type of list(not available keyword so make class of employ)) '''  

''' Operation on Singly link list (SLL
using insertion,deletion,is_empty,traverse)'''

class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class Sll:
    def __init__(self,start=None):
        self.start = start   
    def is_empty(self):
        return self.start == None
    def insert_at_first(self,data):
        n = Node(data,self.start)
        self.start = n
    def insert_at_last(self,data):
        n = Node(data)
        if not self.is_empty():
           temp = self.start
           while temp.next is not None:
              temp = temp.next
           temp.next = n
        else:
            self.start = n
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next 
        return None
    def insert_after(self,temp,data):
       if temp is not None:
           n = Node(data,temp.next)   
           temp.next = n
         
    def print_list(self) :
        temp = self.start  
        while temp is not None:
            print(temp.item,end=" ")
            temp = temp.next
    def delete_first(self):
        if self.start is not None:
         self.start = self.start.next
    def delete_last(self):
        temp = self.start
        if self.start == None:
            pass 
        elif self.start.next is None:
            self.start = None   
        else:
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    def delete_item(self,data):
        temp = self.start
        if self.start is None:
            return None
        elif self.start.next is None:
            self.start.item  == data
            self.start = None
        else:
            if temp.item == data:
                self.start = temp.next
            else:

              while temp.next is not None:
                if temp.next.item == data:
                    temp.next = temp.next.next
                    break
                temp = temp.next
    def __iter__(self):
        return Slliterator(self.start)

class Slliterator:
    def __init__(self,start):
        self.current = start  
    def __iter__(self):
        return self               
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


                


mylist = Sll()
mylist.insert_at_first(20)
mylist.insert_at_last(10)       
mylist.insert_after(mylist.search(20),30)
mylist.insert_after(mylist.search(30),40)
mylist.print_list()
print()
mylist.delete_item(10)
mylist.print_list()

# for x in mylist:
#     print(x,end=" ")

# print()


