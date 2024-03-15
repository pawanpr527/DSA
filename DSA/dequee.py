'''Deque is another variation of queue.
It is a double ended queue.
Deque is a linear data structure.
Both ends can be used for insertion and deletion
Some deque may support random access depending an implementation'''
class Deque:
    def __init__(self):
        self.item = []
        # self.front = []
        # self.rear = []
        self.item_count = 0
    def is_empty(self):
        return len(self.item) == 0  
    def insert_front(self,data):
        self.item.insert(0,data)
    def insert_rear(self,data):
        self.item.append(data)
    def delete_front(self):
        if not self.is_empty():
            return self.item.pop(0)
        else:
            return "Deque is empty"
    def delete_rear(self):
        if not self.is_empty():
            return self.item.pop(-1)
        else:
            return "Deque is empty"
    def size(self):
        return len(self.item)
    def get_front(self):
        if not self.is_empty():
            return self.item[0]
        else:
            return "Deque is empty"
    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            return "Deque is empty"
a1 = Deque()
a1.insert_front(3)
a1.insert_front(4)
a1.insert_front(5)
a1.insert_rear(9)
a1.insert_rear(7)
# a1.delete_front()
   
# a1.delete_rear()
a1.insert_front(8)
print(a1.item)
print(a1.get_front())
print(a1.get_rear())