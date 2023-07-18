leap_yr=input("Enter the leapyr:")
# print(leap_yr)
# type_of_leap_yr=type(leap_yr)
# print(type_of_leap_yr)
int_of_leap_yr=int(leap_yr)
if (int_of_leap_yr)%4==0 and (int_of_leap_yr)%100!=0 or (int_of_leap_yr)%400==0:
    print("It is a leap year")
else:
    print("It is not a leap year")
        
    

