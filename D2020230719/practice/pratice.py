# name="sharmila"
# dic_name={"name":name}
# file=open("/home/user/Documents/karka.txt","r")
# print(file.read())
# for line in file:
#     print(line)

# data=file.read()
# print(data)   

file=open("/home/user/Documents/karka.txt","a")
file.write("hello text editor/n")
file.write("hello")
file.close()
file=open("/home/user/Documents/karka.txt","r")
for line in file:
    print(line.split())
# print(file.read(7))
