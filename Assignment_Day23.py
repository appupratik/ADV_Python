import os
import time
import datetime
import pickle
from threading import Thread

drive_list = ["c","d","f"]
dict1 = {}
temp_dict = {}
def find_data(a):
    res= os.walk(a+":\\")
    print("Process in Drive :",a,":\\....")
    #print("Current Thread:",currentThread())
    for r,d,f in res:
        for i in f:
            temp_dict.setdefault(i,[]).append(r)
    i = 1
    for k,v in temp_dict.items():
        for file in v:
            ag = file+"\\"+k
            dict1[i]=ag
            i = i+1
    pickle.dump(dict1,file_write)
    tt = datetime.datetime.now()
    print(tt-t1)

t1 = datetime.datetime.now()    
file_write = open('dict.txt','wb')

'''
#Single Threading Start
for disk in drive_list:
    print(disk)
    find_data(disk)
#Single Threading End
'''



#'''
#Multi Threading Start
list_thread = []
drivecount = 0
for each in range(len(drive_list)):
    th1 = Thread(target=find_data, args = (drive_list[drivecount],))
    th1.start()
    list_thread.append(th1)
    drivecount = drivecount + 1

for th in list_thread:
    th.join()
#Multi Threading End
#'''



file_write.close()
t2 = datetime.datetime.now()    
print(t2-t1)


