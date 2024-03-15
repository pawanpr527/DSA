class Node:
    def __init__(self,item=None,prev=None,next=None):   
        self.item = item
        self.prev = prev
        self.next = next
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
        self.items = []
    def is_empty(self):
        return self.item_count == 0
    def insert_front(self,data):
        n = Node(data,None,self.front)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prev =n
        self.front = n 
        self.item_count+=1
    def insert_rear(self,data):
        n = Node(data,self.rear)
        if self.is_empty():
            # self.rear.next = n
            self.front =n 
        else:
            self.rear.next = n
        self.rear = n   
        self.item_count+=1
    def delete_front(self):
        if self.is_empty():
               raise Exception("Deque is empty")
        if self.front == self.rear:
            self.front = None
            self.rear = None    
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count-=1 
    def delete_rear(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.item_count-=1
    def get_front(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.rear.item
    def size(self):
        return self.item_count
a1 = Deque()
a1.insert_front(1)
a1.insert_front(2)
a1.insert_front(3)
a1.insert_front(4)
a1.insert_rear(5)
a1.insert_rear(6)
print(a1.items)
print(a1.get_front(),a1.get_rear())                
a1.delete_front()
a1.delete_rear()
print(a1.get_front(),a1.get_rear())

            
