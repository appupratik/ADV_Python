#Assignment1  - Find all occurances of  given object in list or tuple 
print('\n**********************Assignment-1 AS PER LACTURE****************************')
print('**************Find all occurrences of a given item in the list***************\n')
list1 = [1,2,3,4,5,56,6,1,2,3,4,1,3,2,3]
index = []
temp = []
i=0
print(list1,"\n")
#num = int(input("Enter Any Number From List: "))
num = 1
print(f'\nFind "{num}" in the list of {list1}')
def indexFind(i):
    if list1[i]==num:
        a = list1.index(num,i)
        index.append(a)
    else:
        pass

while i<len(list1):
    indexFind(i)
    temp.append(i)
    i = len(temp)

print('\nIndex of 1 is at below Position:\n')
for i in index:
    print("==>",i)
print("\n************************************DONE************************************\n")
#****************************************************************************************
#Assignment2
print("\n********************************Assignment-2********************************\n")
list4 =["192.168.10.9","192.168.10.4","192.168.10.11","192.168.10.35"]
a = []
b = []
def ips(x):
    for i in x:
        l=i.rsplit(".",1)
        a.append(l)

def joinL(x):
    for i in x:
        l=".".join(i)
        b.append(l)

def sumfun(x):
    return int(x[1])
    
print("Before:\t",list4)
ips(list4)
a.sort(key=sumfun)
joinL(a)
list4 = b
print("After:\t",list4)
print("\n************************************DONE************************************\n")
#*****************************************************************************************
#Assignment3
print("\n********************************Assignment-3********************************\n")
list3=[1,2,3,0,2,3,0,1,24,0,1,3,1,0,1,210,1,2,0,45]
print("Before:\t",list3)
list3.sort()
def zeroEnd(x):
    a=[]
    b=[]
    for i in x:
        if i == 0:
            a.append(0)
        else:
            b.append(i)
    b.extend(a)
    return b

list3 = zeroEnd(list3)
print("After:\t",list3)
print("\n************************************DONE************************************\n")

#****************************************************************************************
#Assignment4
print("\n********************************Assignment-4********************************\n")
list2 = [(10,4),(90,3),(9,1),(10,4),(9,5)]
print("Before:\t",list2)
def sumfun(x):
    return sum(x)
list2.sort(key=sumfun)
print("After:\t",list2)
print("\n************************************DONE************************************\n")

#****************************************************************************************
