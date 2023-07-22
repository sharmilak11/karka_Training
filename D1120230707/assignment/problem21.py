import problem7
height=float(input("Your height in m:"))
weight=int(input('Your weight in kg:'))
print("\n")
BMI=problem7.cal(weight/height)
print(BMI)
if BMI<18.5:
    print("BMI category: under weight")
elif BMI>18.5 and BMI<24.9:
    print("BMI category: normal weight") 
elif BMI>25.0 and BMI<9.9:
    print('BMI category: over weight')
else:
    print('obese')           