
print("WELCOME TO MITCHELL'S TINY ADVENTURE")
print('\n')
q1=input("You are in a creepy house! Would you like to go out to mitchell's adventure or into kitchen?")
if q1=='kitchen':
     q2=input("There is a long countertop ith dirty dishes everywhere. off to one side there is,as you expect,a refrigerator.You may open the refrigerator or look in a cabinet.")
     if q2=='refrigerator':
         q3=input("Inside the refrigerator you see food and stuff.It looks pretty nasty.would you like to eat some of the food?") 
     else:
           print("you can't play! you went out of mitchells adventure")    
     if q3=="yes":
            print("you start eating")
     else:
            print("you die of staravation.....eventually.")
else:
        print("You went out of mitchell's tiny")
       
                   