class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    def is_empty(self):
        return self.front == None
    def enqueue(self,data):    #front
        n = Node(data)
        if self.is_empty():
           self.front = n
        else:
            self.rear.next = n 
        self.rear = n
        self.item_count+=1    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_count-=1    
    def get_front(self):
        if not self.is_empty():
            return self.front.item       
        else:
            raise IndexError("Queue is empty")
   
    def get_rear(self):
      if self.is_empty():
          raise IndexError("Queue is empty")
      else:
          return self.rear.item
    def size(self):
        return self.item_count    

c1 = Queue()
c1.enqueue(6)           
c1.enqueue(7)
c1.enqueue(8)
c1.enqueue(9)
c1.enqueue(10)
print(c1.get_front(),c1.get_rear())
c1.dequeue()
print(c1.get_front(),c1.get_rear())
