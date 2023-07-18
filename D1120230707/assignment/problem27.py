print("Ye olde keyhain shoppe\n")
variable=0


def add_keychains():
    
    a=int(input(f'You have {variable}.How many to add?'))
    print("You now have",a,"keychains" )
    
   
def remove_keychains():
    
    a=int(input(f'You have {variable} keychains.How many to add?'))
    print("You now have",a,"keychains" )
    

def view_value():
    
    print(f"You now have {variable}keychains" )
    print(f"keychain cost 10 each\nTotalcost is",10*{variable})
    

def chekout():
    print("CHECKOUT\n") 
    name=int(input("What is your name? "))
    print(f"You have {variable} keychain\nkeychain cost 10\nTotal cost is",variable*10)
    print("Thanks for your order,",name)

while True:
    print('1.Add keychains to order\n''2.Remove keychains from order\n''3.View current order\n''4.checkout') 
    value=int(input('please enter your choice:'))        
    if value==1:
        add_keychains()
    elif value==2:
        remove_keychains()
    elif value==3:
        view_value()
    elif value==4:
        chekout()      
        break

    else:
        print("Invalid errror")