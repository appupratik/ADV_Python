from copy import deepcopy

print()
print('Shallow Copy'.center(50,'*'))
list1 = [10,20,30,[40,50]]
list2 = list1[:]
print("List1: ",list1)
print("List2: ",list2)
print("Id of List1: ",id(list1))
print("Id of List2: ",id(list2))
print("Id of List1[3]: ",id(list1[3]))
print("Id of List2[3]: ",id(list2[3]))
list1.append(60)
list2.append(100)
print(list1)
print(list2)
list1[3].append("Hi")
print(list1)
print(list2)
print('*'*50)

print()
print('Deepcopy'.center(50,'*'),'\n')
list3 = [10,20,30,[40,50]]
list4 = deepcopy(list3)
print("List3: ",list3)
print("List4: ",list4)
print("Id of List3: ",id(list3))
print("Id of List4: ",id(list4))
print("Id of List3[3]: ",id(list3[3]))
print("Id of List4[3]: ",id(list4[3]))
list3.append(60)
list4.append(100)
print(list3)
print(list4)
list3[3].append("Hi")
print(list3)
print(list4)
print('*'*50)



print()
print('Shallow Copy'.center(50,'*'))
dict1 = {1:10,2:20,3:30,4:{40,50}}
dict2 = dict(dict1)
print("Dict1: ",dict1)
print("Dict2: ",dict2)
print("Id of Dict1: ",id(dict1))
print("Id of Dict2: ",id(dict2))
print("Id of Dict1[4]: ",id(dict1[4]))
print("Id of Dict2[4]: ",id(dict2[4]))
dict1[4]={50,60}
dict2[4]=60
print(dict1)
print(dict2)
print("Id of Dict1[4]: ",id(dict1[4]))
print("Id of Dict2[4]: ",id(dict2[4]))
print('*'*50)

print()
print('Deepcopy'.center(50,'*'),'\n')
dict3 = {1:10,2:20,3:30,4:{40,50}}
dict4 = deepcopy(dict3)
print("Dict3: ",dict3)
print("Dict4: ",dict4)
print("Id of Dict3: ",id(dict3))
print("Id of Dict4: ",id(dict4))
print("Id of Dict3[3]: ",id(dict3[3]))
print("Id of Dict4[3]: ",id(dict4[3]))
dict3[4]={50,60}
dict4[4]=60
print(dict3)
print(dict4)
print("Id of Dict3[4]: ",id(dict3[4]))
print("Id of Dict4[4]: ",id(dict4[4]))
print('*'*50)

