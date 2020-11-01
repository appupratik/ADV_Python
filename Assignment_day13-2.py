import os
res= os.walk("C:\\Users\\PRATIK\\Desktop\\PythonCode\\Python1\\test")

dict1 = {}
for r,d,f in res:
    for i in f:
        dict1.setdefault(i,[]).append(r)

file_name = input("Enter the file name: ")
sr = 1
for k,v in dict1.items():
    if file_name.lower() in k.lower():
        for i in range(len(v)):
            print(str(sr).rjust(3)+". ",k,':',v[i])
            sr = sr+1
