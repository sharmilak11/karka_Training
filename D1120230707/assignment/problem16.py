gender=input("What is your gender (M or F):")
namef=input("First name:")
namel=input("Last name:")
age=int(input("Age:"))
print("\n")
if gender=="m" and age>=20:
   name='Mr.'+ namef
else:
   name=namef + namel   
if gender=="f" and age>=20:
    married=input(f"Are you married,{namef}(y or n)?\n")
    if married=="yes":
     name="Mrs."+ namef
    else:
        name="Ms."+ namef
elif gender=='f' and age<20:
   name=namef + namel
print(f"Then I shall call you {name}.")

