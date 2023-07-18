print("Ye olde keyhain shoppe\n")

def main_funtion() :
    print('1.Add keychains to order\n''2.Remove keychains from order\n''3.View current order\n''4.checkout') 
    value=int(input('please enter your choice:'))             
    if value==1:
        add_keychains()
    elif value==2:
        remove_keychains()
    elif value==3:
        view_value()
    else:
        chekout()  

def add_keychains():
    print("ADD KEYCHAINS")
    main_funtion()
   
def remove_keychains():
    print("REMOVE KEYCHAIN")
    main_funtion() 

def view_value():
    print("VIEW ORDER")
    main_funtion() 

def chekout():
    print("CHECKOUT")  
main_funtion()