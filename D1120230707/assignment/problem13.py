def little_quiz(q1,q2):
    if q1=="animal":
        if q2=="yes":
             print("My guess is that you are thinking of a squirrel.\nI would ask you if I'm right,but I don't actually care")
        else:
            print("My guess is that you are thinking of a mouse.\nI would ask you if I'm right,but I don't actually care")
    elif q1=="vegetable":
        if q2=="yes":
            print("My guess is that you are thinking of a watermelon.\nI would ask you if I'm right,but I don't actually care")
        else:
            print("My guess is that you are thinking of a carrot.\n I would ask you if I'm right,but I don't actually care")
    elif q1=="minerals":
        if q2=="yes":
            print("My guess is that you are thinking of a camaro.\nI would ask you if I'm right,but I don't actually care")                      
        else:
            print("My guess is that you are thinking of a paper lclip.\nI would ask you if I'm right,but I don't actually care")     
print("TWO QUESTIONS!\nThink of an object,and I'll try to guess it.")
q1=input("Question 1) Is it animal,vegetable or mineral?\n\t>")
q2=input("Question 2) Is it bigger than a breadbox?\n>")
a=little_quiz(q1,q2)
