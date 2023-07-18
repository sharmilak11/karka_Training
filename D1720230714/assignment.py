# personal_details=[{"name":"sharmila","age":20,"place":"nettankodu"},{"name":"sowmiya","age":21,"place":"nagercoil"},{"name":"vidhya","age":21,"place":"vadasery"}]
# def details(personal_details):
#  for i in range(0,len(personal_details)) :
#   a=personal_details[i]["name"]
#   b=personal_details[i]["age"]
#   c=personal_details[i]["place"]
#   print("Iam",a,",Iam",b,"years old,and Iam from",c)
# details(personal_details)

# def age(personal_details):
#  for i in range(0,len(personal_details)):
#   a=personal_details[i]['age']
#   b=personal_details[i]['name']
#   c=personal_details[i]['place']
#   if a>=21:
   # print(b,"from",c)
# age(personal_details)

cricket_players=[{"name":"babar azam","no_of_centuries":27,"half centuries":26,"wicket taken":2,"hat-trick wickets":0,"top batting scores":[158,200,100,150]},{"name":"dhananjaya de silva","no_of_centuries":9,"half centuries":10,"wicket taken":41,"hat-trick wickets":20,"top batting scores":[93,67,90,100]},{"name":'johson charles','no_of_centuries':2,"half centuries":7,"wicket taken":0,"hat-trick wickets":1,"top batting scores":[16,20,89,45]},{"name":"scott edward",'no_of_centuries':0,"half centuries":13,"wicket taken":78,"hat-trick wickets":18,"top batting scores":[86,90,120,100]},{"name":"dhoni","no_of_centuries":10,"half centuries":73,"wicket taken":1,"hat-trick wickets":20,"top batting scores":[224,100,300,150]}]
def cricket(cricket_players):
   b=0
   for i in range(0,len(cricket_players)):
      a=cricket_players[i]["no_of_centuries"]
      no_of_players=0
      if a>10:
         no_of_players=no_of_players+1
         print(f"no_of_players:{no_of_players}")
      elif i["hat-trick wickets"]>5:
       print( i["name"] "have taken more than 5 hat tricks wickets") 
      else:
         a=i['top batting scores']
      for c in a:
         if b<c:
            b=c
      
      print(f"top batting scores:player {b}")
      b=0
cricket(cricket_players)

 
