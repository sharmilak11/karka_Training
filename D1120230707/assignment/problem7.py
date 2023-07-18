def BMI_calculate():
    height=float(input("Your height in m:"))
    Weight=int(input("Your weight in kg:"))   
    tot=(Weight)/height**2
    return tot
cal=BMI_calculate()
print('Your BMI is',cal )   