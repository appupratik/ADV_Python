list1 = [10,20,30,40,50,60,70]
list2 = [5,15,25,35,36,37,38,39,80]

list3 = []

while list1 and list2:
    if list1[0] <= list2[0]:
        i = list1.pop(0)
        list3.append(i)
    else:
        i = list2.pop(0)
        list3.append(i)

#list3.extend(list1)
#list3.extend(list2)
print(list3)