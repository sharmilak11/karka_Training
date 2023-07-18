a=int(input("enter value:"))
b=int(input("enter value:"))
c=int(input("enter value:"))

def triangle(a,b,c):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**1/2
    return area 
a=triangle(a,b,c)
print("Area of the triangle",a)



def square():
    side=int(input("enter value"))
    area=side*side
    return area
a=square()
print('Area of the square',a)
def rectangle():
    length=int(input("enter value"))
    breath=int(input("enter value"))
    area=length*breath
    return area
area=rectangle()
# print("area of the rectangle",area)
def circle():
    r=int(input("enter value:"))
    area=3.14*r**2
    return area
a=circle()
print("Area of the circle",a)

def trapezium():
    a=int(input("enter value:"))
    b=int(input("enter value:"))
    height=int(input("enter value:"))
    area=((a+b)*height)*1/2
    return area
trapezium()
print("Area of the trapezium",a)