import random


str1 = ['ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','0123456789','!@#$%^&*']
res1=[]

def generatePwd():
    res1=[]
    for i in range(6):
        a = random.choice(str1[0])
        res1.append(a)
    for i in range(4):
        a = random.choice(str1[1])
        res1.append(a)
    for i in range(2):
        a = random.choice(str1[2])
        res1.append(a)
    random.shuffle(res1)
    return "".join(res1)

print("First Random Password is \t: ",generatePwd())
print("Second Random Password is \t: ",generatePwd())
print("Third Random Password is \t: ",generatePwd())
print("Forth Random Password is \t: ",generatePwd())
