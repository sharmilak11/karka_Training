print("I will add up the number you give me:")
num=int(input("number:"))
total=num

for i in range(100):
   num=int(input("Number"))
   if num==0:
      break
   else:
      total=total+num
      print("The total so far is",total)

print("The total is",total)

   
   
   

