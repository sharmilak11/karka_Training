consumer_data={"consumer_name":"abi",
               "EB_reading":[1100,1200,1350,1650,2050]}

def calculate_electricity_bill(consumer_data):
      month=0
      bill=0
      for i in range(0,len(consumer_data['EB_reading'])-1):  
            month=i+1      
            a=consumer_data["EB_reading"][i+1]-consumer_data['EB_reading'][i]
            # print(a)
            if a<100:
                  print(f"month:{month}\nunits_consumed:{a}\nbill_amount:{bill}")
            elif a>=100 and a<200:
                  value=a*2
                  bill=bill+value
                  print(f"month:{month}\nunits_consumed:{a}\nbill_amount:{value}")

            elif a>=200 and a<500:
                  value=a*5
                  bill=bill+value
                  print(f"month:{month}\nunits_consumed:{a}\nbill_amount:{value}")

            elif a>=500 and a<1000:
                  value=a*10
                  bill=bill+value
                  print(f"month:{month}\nunits_consumed:{a}\nbill_amount:{value}")

            else:
                  value=a*14
                  bill=bill+value
      print(f"total_amount:{bill}")
calculate_electricity_bill(consumer_data)

            