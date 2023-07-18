def quiz(q1,q2,q3):
    a=0
    if q1==3:
        a=a+1
        print("That's right!")
    if q1!=3:
        print("That's wrong")
    if q2==2:
        a=a+1
        print("That's right")
    if q2!=2:
        print("sorry,cat is a string .ints can only store numbers.")
    if q3==2:
        a=a+1
        print("That's right")
    if q3!=2:
        print("That's wrong")
    return a  
reply=input("Are you ready for a quiz?") 
print("okay,here it comes!") 
q1=int(input("Q1) What is the capital of Alaska?\n\t1)Melbourne\n\t2)Anhoragen\t3)Juneau\n>")) 
q2=int(input("Q2) Can you store the value cat in a variable of type int?\n\t1)Yes\n\t2)No\n>"))
q3=int(input("Q3) What is the result of 9+6/3\n\t1)5\n\t2)11\n\t3)15/3\n>"))   
a=quiz(q1,q2,q3)      
print(f'Overall,you got{a}out of 3 correct.') 
