a=16
for i in range(1,16):
        if i%3==0 and i%5==0:
            print(i,"fizzbizz")
        elif i%3==0:
            print(i,"fizz")
        elif i%5==0:
            print(i,"bizz")               
        else:
             print(i)