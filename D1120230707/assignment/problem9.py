def weekday(day):
    if day==0 and day==7:
        print('Today is Satursday')
    elif day==1:
        print("Today is Sunday")  
    elif day==2:
        print("Today is Monday")
    elif day==3:
        print("Today is Tuesday")
    elif day==4:
        print('Today is Wednesday') 
    elif day==5:
        print("Today is Thursday")
    elif day==6:
        print("Today is Friday")
    else:
        print("Error")
a=int(input('Enter a day:'))
final=weekday(a) 
  

                         