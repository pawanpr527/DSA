def bubble_sort(data_list):
    for j in range(1,len(data_list)):
        for i in range(len(data_list)-j):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
def modified_bubble_sort(data_list):
    flag = False
    for j in range(1,len(data_list)):
        for i in range(len(data_list)-j):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]  
                flag = True
        if not flag:
                break                  
n = int(input("Enter size of list : "))
y = []
for i in range(n):
    data = int(input("Enter element : "))
    y.append(data)
print(y)    
modified_bubble_sort(y) 
print(y)  

