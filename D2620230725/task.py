# import datetime
# var=datetime.datetime.now()
# name=input("enter your name:")
# hour_cal=var.hour
# if hour_cal>6 and hour_cal<12:
#     print(f"Good morning! {name}")
# elif hour_cal>12 and hour_cal<3:
#     print(f"Good afternoon! {name}")    
# elif hour_cal>4 and hour_cal<6:
#     print(f"Good evening! {name}")
# else:
#     print(f"Good night! {name}")
    
# n=5
# for i in range(n):
#     # print("*"*5)
#     for j in range(n):
#         # print(j)
#         print("*",end=" ")
#     print(" ")   

# n=5
# vr=1

# for i in range(n):
#     # print(n)
#     for j in range(n):
#         print(vr,end=" ")
#         vr=vr+1
#     print(" ") 
n=5
# for i in range(n*n,0,-1):
#     if i%n==0:
#      print("")
#     print(i,end=" ")
# import datetime
# a=datetime.datetime.now() 
# print(type(a))  
# da="24/12/2022 10:12:05"
# var=datetime.datetime.strptime(da,"%d,/%m/%y %H:%M:%S")
# print(type(var))
# print(var)

from datetime import datetime,timedelta

date_string = "21 June, 2018"

print("date_string =", date_string)
print("type of date_string =", type(date_string))

date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

date=date_object+timedelta(days=2)