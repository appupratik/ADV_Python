#Question 1
#The SHIELD is a secretive organization entrusted with the task of guarding the world against any disaster. Their arch nemesis is the organization called HYDRA. Unfortunately some members from HYDRA had infiltrated into the SHIELD camp. SHIELD needed to find out all these infiltrators to ensure that it was not compromised. Nick Fury, the executive director and the prime SHIELD member figured out that every one in SHIELD could send a SOS signal to every other SHIELD member he knew well. The HYDRA members could send bogus SOS messages to others to confuse others, but they could never receive a SOS message from a SHIELD member. Every SHIELD member would receive a SOS message ateast one other SHIELD member, who in turn would have received from another SHIELD member and so on till NickFury. SHIELD had a sophisticated mechanism to capture who sent a SOS signal to whom. Given this information, Nick needed someone to write a program that could look into this data and figure out all HYDRA members.

#Sample Input
'''
Nick Fury : Tony Stark, Maria Hill, Norman Osborn
Hulk : Tony Stark, HawkEye, Rogers
Rogers : Thor,
Tony Stark: Pepper Potts, Nick Fury
Agent 13 : Agent-X, Nick Fury, Hitler
Thor: HawkEye, BlackWidow
BlackWidow:Hawkeye
Maria Hill : Hulk, Rogers, Nick Fury
Agent-X : Agent 13, Rogers
Norman Osborn: Tony Stark, Thor
'''
#Sample Output
#Agent 13, Agent-X, Hitler

dict1 = {   'Nick Fury': ['Tony Stark', 'Maria Hill', 'Norman Osborn'],
            'Hulk' : ['Tony Stark', 'HawkEye', 'Rogers'],
            'Rogers' : ['Thor'],
            'Tony Stark': ['Pepper Potts', 'Nick Fury'],
            'Agent 13' : ['Agent-X', 'Nick Fury', 'Hitler'],
            'Thor': ['HawkEye', 'BlackWidow'],
            'BlackWidow':['Hawkeye'],
            'Maria Hill' : ['Hulk', 'Rogers', 'Nick Fury'],
            'Agent-X' : ['Agent 13', 'Rogers'],
            'Norman Osborn': ['Tony Stark', 'Thor']
            }

list1 = []
list2 = []

list1.append(('Nick Fury',1))
for el in dict1['Nick Fury']:
    list1.append((el,0))
    
for k,v in enumerate(list1):
    if list1[k][1] == 0:
        temp = list(list1[k])
        temp[1] = 1
        list1[k] = tuple(temp)
        if list1[k][0] in dict1.keys():
            for el in dict1[list1[k][0]]:
                addVal = 0
                for item in list1:
                    if item[0] == el:
                        addVal = 1
                        break

                if addVal == 0:
                    list1.append((el,0))

for key in dict1.keys():
    for val in dict1[key]:
        if val not in list2:
            list2.append(val)

final_list, addVal = zip(*list1)
final_list = list(final_list)
   
for person in final_list:
    list2.remove(person)

list2.sort()

print ('\nMembers of HYDRA are:')
a = 1
for i in list2:
    print("\t",a,i)
    a +=1