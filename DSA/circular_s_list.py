class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next


class CSL:
    def __init__(self,last=None):
        self.last= last
    def is_empty(self):
        return self.last == None
                
    def insert_at_start(self,data):
        n = Node(data)
        if self.is_empty():
          n.next = n
          self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last  = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n 
    def search(self,data):
        temp = self.last.next
        if self.is_empty():
            return None
        elif temp is self.last:
           if temp.item == data:
              return temp
        else:
         while temp is not self.last:
               if temp.item == data:
                   return temp
               temp = temp.next            
      #   if temp.item == data:
      #       return temp
        return None
    def insert_after(self,temp,data):
      if temp is not None:
        if temp is not self.last:
            n = Node(data,temp.next)
            temp.next = n
        else:
           n = Node(data,temp.next)
           temp.next = n
         #   n.next = temp
            # if temp.next is self.last:
            #    self.last = n
    def print_list(self):
     if not self.is_empty():  
        temp = self.last.next
        while temp != self.last:
            print(temp.item,end=" ")
            temp = temp.next
        print(temp.item)
    def delete_first(self):
     if not self.is_empty():
      if self.last.next == self.last:
        self.last = None
      else:
        self.last.next = self.last.next.next 
    def delete_last(self):
       if not self.is_empty():
          if self.last.next == self.last:
             self.last = None
          else:
            temp = self.last.next
            while temp.next is not self.last:
              temp = temp.next
            temp.next = self.last.next
            self.last = temp
    def delete_item(self,data):
       if not self.is_empty():
         #  if self.last.next == self.last:
         #     if self.last.item == data:
         #        self.last = None
         #  else:
             if self.last.next.item == data:
                self.delete_first()
             else:
                temp = self.last.next
                while temp is not self.last:
                 if temp.next== self.last:
                    if self.last.item==data:
                      self.delete_last()
                      break
                 if temp.next.item == data:
                     temp.next = temp.next.next
                     break
                 temp = temp.next
    def __iter__(self):
       if self.last == None:
          return Cslliterator(None)
       else:
          return Cslliterator(self.last.next)             

class Cslliterator:
   def __init__(self,start): 
      self.current = start  
      self.start = start  
      self.count = 0
   def __iter__(self):
      pass              
   def __next__(self):
      if self.current is None:
         raise StopIteration
      if self.current == self.start and self.count==1:
         raise StopIteration 
      else:
         self.count = 1
      data = self.current.item
      self.current = self.current.next      
      return data   

cll = CSL()
cll.insert_at_start(2)
cll.insert_at_start(1)
cll.insert_at_start(3)
cll.insert_at_start(4)
cll.insert_at_last(6)
cll.insert_at_last(7)
cll.insert_after(cll.search(1),9)

for x in cll:
   print(x,end=" ")
print()   
# cll.delete_first()
# cll.delete_last()
cll.delete_item(4)
cll.delete_item(2)
cll.print_list()
# cll.print_list()