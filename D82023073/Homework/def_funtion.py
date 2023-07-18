# homework
def operating(a,b,c):
    if b=="+":
        return a+c
    if b=="-":
         return a-c 
    if b=="*":
        return a*c
    if b=="/":
        return a/c
    if b=="%":
        return a%c
a=int(input("Enter a first number:"))
b=input("Enter the operations:")
c=int(input("Enter a another number:"))
operate=operating(a,b,c)
print(operate)

