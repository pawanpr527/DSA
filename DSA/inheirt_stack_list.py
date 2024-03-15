class stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
     try: 
         if not self.is_empty():
           return self[-1]  
         else:
           raise IndexError("Stack is empty")
     except IndexError:
      print("Stack is empty")
    
      def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("Stack is not support insert method")
s1 = stack()
print(s1.peek()) 
s1.push(11)   
s1.push(12) 
s1.push(13) 
s1.push(14) 
s1.push(15) 
print(s1.peek())
        
        