print("Ye olde keyhain shoppe\n")
your_cart=0
sales_tax=8.25
shipping_cost=5.00
keychain_shipping_cost=1.00

def add_keychains(your_cart):
    print("ADD KEYCHAINS")
    add=int(input("You have 0 keychains. How many to add?"))
    your_cart=your_cart+add
    print(f"You now have {your_cart} keychains" )
    return your_cart
   
def remove_keychains(your_cart):
    print("REMOVE KEYCHAINS")
    add=int(input("You have 0 keychains. How many to remove?"))
    your_cart=your_cart-add
    print(f"You now have {your_cart} keychains" )
    return your_cart

def view_value(shipping_cost,sales_tax,keychain_shipping_cost,your_cart):
    print('VIEW ORDER')
    total1=your_cart*10
    shipping_charge=shipping_cost+(your_cart*keychain_shipping_cost)
    tax=total1*sales_tax
    total_cost=total1+shipping_charge+tax
    print(f"You now have {your_cart} keychains\nkeychains cost $10 per each\nshipping charges{shipping_charge}" )
    return your_cart

def chekout(shipping_cost,sales_tax,your_cart):
    print("CHECKOUT\n") 
    name=int(input("What is your name? "))
    view_value(shipping_cost,sales_tax,keychain_shipping_cost)
    print("Thanks for your order,",name)
    return your_cart


while True:
 print('1.Add keychains to order\n''2.Remove keychains from order\n''3.View current order\n''4.checkout') 
 value=int(input('please enter your choice:'))             
 if value==1:
        your_cart=add_keychains(your_cart)
 elif value==2:
        your_cart=remove_keychains(your_cart)
 elif value==3:
        your_cart=view_value(your_cart,shipping_cost,sales_tax,keychain_shipping_cost)
 elif value==4:
        your_cart=print(your_cart,shipping_cost,sales_tax)
        break
 else:
        print("Invalid choise")    
        
