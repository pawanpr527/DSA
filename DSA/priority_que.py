class priorityQ:
    def __init__(self):
        self.item = []
    def is_empty(self):
        return len(self.item)==0    
    def push(self,data,priority):
        index = 0   #This priority based on rank, means 1 have highest priority and 10+ have lowest 
        while index<len(self.item) and self.item[index][1]<=priority:
            index+=1
        self.item.insert(index,(data,priority))    
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        return self.item.pop(0)[0]
    def size(self):
        return len(self.item)
p = priorityQ()
p.push("Pawan",5)
p.push("dheeraj",9)
p.push("hitsh",1)  
p.push("arjun",2)
p.push("harsh",6)
p.push("bha",7)  
p.pop()
while not p.is_empty():
    print(p.pop())
print()
