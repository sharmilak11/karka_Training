name=[{"name":"sivaraj","place":"nagercoil","hobbies":["circket","movies","music"],"SSLC":{"tamil":67,"english":90,"maths":76,"science":77,"social":90}},{"name":"sharmila","place":"mondaymarket","hobbies":["cooking","movies","temple"],"SSLC":{"tamil":78,"english":90,"maths":80,"science":70,"social":97}},{"name":"alfeeda","place":"tambaram","hobbies":["planting","music","series"],"SSLC":{"tamil":67,"english":90,"maths":89,"science":77,"social":90}},{"name":"akashaya","place":"theerur","hobbies":["music","phone","series"],"SSLC":{"tamil":67,"english":90,"maths":75,"science":77,"social":90}},{"name":"bharathi","place":"thoovali","hobbies":["eating","sleeping",'phone'],"SSLC":{"tamil":67,"english":90,"maths":92,"science":77,"social":90}},{"name":"sanjay","place":"nageroil","hobbies":["utube","music","movies"],"SSLC":{"tamil":54,"english":90,"maths":89,"science":70,"social":97}}]
# find total of each sslc
for i in name:
    total=0
    a=i["SSLC"]["tamil"]+i["SSLC"]["english"]+i["SSLC"]["maths"]+i["SSLC"]["science"]+i["SSLC"]["social"]
    total=total+a
    print(total)
    
# total more than 90%
    b=i['SSLC']["maths"]
    average=total/5
    if average>90:
        print("you are eligible for maths biology")
    elif average>80:
        print("you are eligible for computer science")
    elif average>75 and b>98 :
        print("you are eligible for maths biology")
    elif average>70 and b>98: 
        print("you are eligible for computer science")             
    
