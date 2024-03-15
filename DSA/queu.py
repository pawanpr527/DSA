class Queue:
    def __init__(self):
        self.item = []

        self.count = 0
    def is_empty(self):
        return self.item == []
    def enqueue(self,data):
    #    if not self.is_empty(): 
          self.item.append(data)
          self.count +=1    
          #else:
          #   raise IndexError("Queue is empty")
    def dequeue(self):
         if not self.is_empty():
              return self.item.pop(0)  # Remove first element
         else:
              raise IndexError("Queue is empty")
    def get_front(self):
         if not self.is_empty():
              return self.item[0]
         else:
              raise IndexError("Queue is empty")    
    def get_rear(self):
         if not self.is_empty():
              return self.item[-1]
         else:
              raise IndexError("Queue is empty")
    def size(self):
         return len(self.item)     

A1 = Queue()         
A1.enqueue(10)
A1.enqueue(9)
A1.enqueue(8)
A1.enqueue(7)
print(A1.item)
# print(A1.size())
print(A1.get_front(),A1.get_rear())
A1.dequeue()
print(A1.get_front(),A1.get_rear())



