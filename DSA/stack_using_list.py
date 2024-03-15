class list:
    def __init__(self):
        self.items = []
        self.add = []
    def is_empty(self):
        return len(self.items) == []
    def push(self,data):    #to insert data in stack
        self.items.append(data)
    def pop(self):
       if not self.is_empty():    #to delete data from stack
         return self.items.pop()
       else:
           raise IndexError("Stack is empty")
    def peek(self):   #to see the top of stack
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self.items)
    def adds(self,data):
        if not self.is_empty():
          self.add.append(data)
        else:
            raise TypeError("Stack is empty") 
    def exte(self):
        return self.items.extend(self.add)       

s1 = list()
s1.push(10)
s1.push(9)  
s1.push(8)  
s1.push(7)  
s1.push(6)  
s1.push(5)  
s1.push(4)  
s1.push(3)  
s1.push(2)  
s1.push(1)

s1.adds(11)
s1.adds(12)
s1.exte()
# s1.add(13)
# s1.add(14)

print(s1.peek())
print(s1.size())
# # print(s1.pop())
# print(s1.pop())


