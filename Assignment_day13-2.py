import os
res= os.walk("C:\\Users\\PRATIK\\Desktop\\Python\\test")

dict1 = {}
for r,d,f in res:
    for i in f:
        dict1.setdefault(i,[]).append(r)

file_name = input("Enter the file name: ")
for k,v in dict1.items():
    if file_name.lower() in k.lower():
        for i in range(len(v)):
            print(k,':',v[i])
