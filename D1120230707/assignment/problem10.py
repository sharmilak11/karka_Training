def age_message(age):
    if age<16:
        return ("You can't drive.")
    elif age==16 or age<=17:
        return("You can drive but not vote.")
    elif age<=18 or age<=24:
        return("You can vote but not rent a car")
    else:
        return("You an do pretty much anything.")
enter=input("Hey, What's your name? (Sorry,I keep forgetting.)")  
age=int(input(f"Ok,{enter},how old are you?"))    
eligible=age_message(age) 
print(eligible,enter)