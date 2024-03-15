# from array import *
# a1 = array('i',[5,8,3,2])  #  // i is type code (signed integer)
# print(a1)
# for i in a1:
#     print(i,end=" ")

# for y in range(len(a1)):
#     print(a1[y],end=" ")   

# # All methods are like list example = append,count,extend,index,fromlist,insert,pop
#     #remove,reverse,tolist    

# print(sum(a1))

"""Priority Queue"""
class PriorityQ:
    def __init__(self):
        self.item = []
    def is_empty(self):
        return len(self.item) == 0
    def push(self,data,priority):
        index = 0 
        while index<len(self.item) and self.item[index][1]<=priority:
            index+=1
        self.item.insert(index,(data,priority))  
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        return self.item.pop(0)
    def size(self):
        return len(self.item)
a1 = PriorityQ()
a1.push(3,5)
a1.push(8,8)
a1.push(4,4)
a1.push(2,1)    
a1.push(2,8)
a1.push(9,2)
while not a1.is_empty():
    print(a1.pop())
print()    
