# consumer_data={"consumer_name":"abi",
            #    "EB_reading":[1100,1200,1350,1650,2050]}
units=[]

month=0
bill=0
for i in range(0,len(['EB_reading'])-1): 
            dict={} 
            month=i+1      
            a=["EB_reading"][i+1]-['EB_reading'][i]
            if a<100:
                  print(f"month:{month}\nunits_consumed:{a}\nbill_amount:{bill}")
            elif a>=100 and a<200:
                  value=a*2
                  bill=bill+value
            elif a>=200 and a<500:
                  value=a*5
                  bill=bill+value
            elif a>=500 and a<1000:
                  value=a*10
                  bill=bill+value
            else:
                  value=a*14
                  bill=bill+value
            dict={"month":i+1,"units_consumed":a,"total_amount":value}       
            units.append(dict)
print(units)


# list_string=str(units)
# print(list_string)
# name=consumer_data["consumer_name"]
# file=open(f"/home/user/Documents/{name}.txt","w")
# file.write(list_string)
# file.close()
# file=open(f"/home/user/Documents/{name}.txt","r")
# file=open(f"/home/user/Documents/{name}.txt","w")     

# for i in units:
      # print(i)
#       month=i['month']
#       units_consumed=i['units_consumed']
#       total_amount=i['total_amount']
#       a=(f"month:{month}\nunits_consumed:{units_consumed}\ntotal_amount:{total_amount}\n")
#       file.write(a)
# file.close()
# file=open(f"/home/user/Documents/{name}.txt","r")

import json
name=input('enter your name:')
eb_reading1=int(input('enter the first reading:'))
eb_reading2=int(input('enter the second reading:'))
eb_reading3=int(input('enter the third reading:'))
eb_reading4=int(input('enter the fourth reading:'))
consumer_data={"consumer_name":name,"Reading":[eb_reading1,eb_reading2,eb_reading3,eb_reading4]}
choice=input("enter your choice?")
if choice=="json" and "JSON" and "Json" and "jsOn" and "JSon":
       lst_json=json.dumps(name)
       print(lst_json)
elif choice=="dict":
       lst_dict=str(units)
       print(lst_dict)       


for i in units:
       file=open(f"/home/user/Documents/{name}.txt","r")
       file.write(lst_dict)
       file.close()
file=open(f"/home/user/Documents/{name}.txt","r")



      
