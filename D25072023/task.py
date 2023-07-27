monthly_gold_rate=[{"month":"january","gold_rate":1000,
                    "jewel_list":[{"name":"chain","making_cost":12},
                                  {"name":"earing","making_cost":13}]},
                {"month":"febuary","gold_rate":2000,
                 "jewel_list":[{"name":"ring","making_cost":12},
                                  {"name":"bangles","making_cost":13}]},
                {"month":"march","gold_rate":1500,
                 "jewel_list":[{"name":"chain","making_cost":10},
                                  {"name":"ring","making_cost":13}]},
                {"month":"april","gold_rate":200,
                 "jewel_list":[{"name":"chain","making_cost":12},
                                  {"name":"earing","making_cost":13}]}]

# lst=[]
# for i in monthly_gold_rate:
#     month=i["month"]
#     gold_rate=i["gold_rate"]
#     for j in i["jewel_list"]:
#      name=j["name"]
#      cost=j["making_cost"]    
#      val=gold_rate*cost/100
    #  total_rate=gold_rate+val
    #  var=(f"month:{month},gold_rate:{gold_rate},{name},total_rate{total_rate}")
    #  dit={f"month:{month},gold_rate:{gold_rate},name:{name},total_rate:{total_rate}"}
    #  print(dit)
    #  lst.append(var)

from datetime import date
curr_date=date(2023,7,25)
print(curr_date)
curr_date=date.today()
print(curr_date)
curr_date=date.today().year
print(curr_date)
curr_date=date.today().month
print(curr_date)
from datetime import time
vari=time(12,15,7)
print(time)
time=time.hour
print(time)
time=vari.second
print(time)
from datetime import datetime
curr_date=datetime(2023,7,25,11,12,7)
print(curr_date)
# curr_dateyt=curr_date.time
cur=datetime.now()
print(cur)
c=cur.strftime("%y")
print(c)
c=cur.strftime("%m")
print(c)
c=cur.strftime("%h")
print(c)
c=cur.strftime("%M")
print(c)
c=cur.strftime("%d")
print(c)
c=cur.strftime("%D")
print(c)
c=cur.strftime("%Y")
print(c)
c=cur.strftime("%H")
print(c)
import pytz
var=pytz.timezone("asia/kolkata")
c=datetime.now(var)
print(c)
from datetime import datetime
from pytz import timezone
 
format = "%Y-%m-%d %H:%M:%S %Z%z"
 
now_utc = datetime.now(timezone('UTC'))
print(now_utc.strftime(format))
 
# Convert to Asia/Kolkata time zone
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
print(now_asia.strftime(format))

# timezone=pytz("asia")
# val=datetime.now(timezone())
# c=val.strftime("%y-%m-%D %")