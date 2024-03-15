#calculate sum of first n Odd number
def Sum(n):
   if n == 0:   
      return 0
   elif n == 1:
      return 1
   return (2*n-1)+Sum(n-1)

x = int(input("Enter the number: "))
if x<0:
   print("Invalid input")
else:
    if x == 0:
       pass
    elif x == 1:
       print("Sum is 1")
    else:
      y = Sum(x)
      print("Sum is ",y)

def sumEven(n):  
   if n == 0:
        return 0
   return 2*n+sumEven(n-1)
                      
print(sumEven(10))

def fact(n):
    if n<0:
        return None
    else:
        if n==0:
            return 1
        return n*fact(n-1)
print(fact(10))        

# calculate Sum of first n square natural number
def sumSquare(n):
    if n==0:
        return 0
    return n**2+sumSquare(n-1)
print(sumSquare(5))
