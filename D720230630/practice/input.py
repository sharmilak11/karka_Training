# # input("which year you passed out from college:")
passed_out_yr=input("Which year you passed out from college:")
# print(passed_out_yr)
type_of_passed_out_yr=type(passed_out_yr)
print(type_of_passed_out_yr)
# int_passed_out_yr=int(passed_out_yr)
# print(type(int_passed_out_yr))

is_eligible=passed_out_yr>="2021" and passed_out_yr<="2023"
if is_eligible:
    print("person is eligible" )
else:
    print("person is not eligible")
print('hello')


