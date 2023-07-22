# height=float(input("Your height in m:"))
# Weight=int(input("Your weight in kg:"))   

def BMI_calculate(weight,height):
    tot=(weight)/height**2
    return tot
cal=BMI_calculate()
print('Your BMI is',cal )   