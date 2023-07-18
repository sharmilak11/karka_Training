def age_old():
    name=input("Hey, what's your name?")
    old=int(input(f"Ok,{name},how old are you?"))
    if old<16:
        print( f'you cant drive,{name}')
    if old<18:
        print(f'you cant vote,{name}')
    if old<25:
        print(f'you cant rent a car,{name}')
age=age_old()
