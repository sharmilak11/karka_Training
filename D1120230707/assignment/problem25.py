def month_name(name):
      if name==1:
         return "January" 
      elif name==2:
         return "Febuary"
      elif name==3:
         return "March"
      elif name==4:
         return "April"
      elif name==5:
         return "May"        
      elif name==6:
         return "June"
      elif name==7:
         return "July" 
      elif name==8:
         return "Augest"
      elif name==9:
         return"September" 
      elif name==10:
         return "October"
      elif name==11:
         return "November"
      elif name==12:
         return "December"             
      else:
         return "Error"  
name=int(input("enter month :"))         
a=month_name(name)         
print(a)