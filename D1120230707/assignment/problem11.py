def Weight(a):
    mars_gravity=0.39
    b=float(a*mars_gravity)
    if a==1:
        return 0.78
    if a==2:
        return 0.39
    if a==3:
        return 2.65
    if a==4:
        return 1.17
    if a==5:
        return 1.05
    else:
        return 1.23
a=int(input("Please enter your current earth weight:"))
b=Weight(a) 
print("I have information for the following planets:\n\t1.venus  2.Mars  3.Jupiter\n\t4.Saturn  5.Uranus  6.Neptune")
print("\n")
visit=int(input("Which planet are you visiting?"))
print("\n")
print(f"Your weight would be {b} pounds on that planets.")
