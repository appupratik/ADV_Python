import datetime

main_list = list(range(100000000))
t1 = datetime.datetime.now()
#list1 = [each**2 for each in main_list]
list1 = (each**2 for each in main_list)
for each in list1:
    each
t2 = datetime.datetime.now()
print(t2-t1)


'''
........My Findings ........
============================
1.
Traceback (most recent call last):
  File "assignment.py", line 5, in <module>
    list1 = [each**2 for each in main_list]
  File "assignment.py", line 5, in <listcomp>
    list1 = [each**2 for each in main_list]
MemoryError

2.
Traceback (most recent call last):
  File "assignment.py", line 5, in <module>
    list1 = [each**2 for each in main_list]
  File "assignment.py", line 5, in <listcomp>
    list1 = [each**2 for each in main_list]
MemoryError

3.
Traceback (most recent call last):
  File "assignment.py", line 5, in <module>
    list1 = [each**2 for each in main_list]
  File "assignment.py", line 5, in <listcomp>
    list1 = [each**2 for each in main_list]
MemoryError

**************************************************
1.  0:01:06.331647
2.  0:01:07.836592
3.  0:01:10.949460
'''