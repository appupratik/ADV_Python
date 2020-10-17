import time, calendar

a = "15-08-2020 15:02:20"

def human_epoch(a):
    t1 = time.strptime(a, "%d-%m-%Y %H:%M:%S")
    t2=time.mktime(t1)
    t2 =int(t2)
    
    t3 = calendar.timegm(t1)
    
    return t2,t3


result = human_epoch(a)

print("GMT TimeZone  :\t\t",result[1])
print("Local TimeZone :\t",result[0])
