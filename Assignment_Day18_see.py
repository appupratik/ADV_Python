##command line   >>   python see1.py -ri "def sum" C:\Users\PRATIK\Desktop\PythonCode
##Output         >>   Total files checked: 112 & Total Matches found: 6.

##command line   >>   python see1.py -si "def sum" C:\Users\PRATIK\Desktop\PythonCode
##Output         >>   Total files checked: 31 & Total Matches found: 4.
import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-si',nargs=2, metavar=('Pattern,','\tSearch Path'))
parser.add_argument('-ri',nargs=2, metavar=('Pattern,','\tSearch Path'))
args = parser.parse_args()	

def err():
    os.system('cls')
    print('\n'+'*'*75+'\n')
    print("Please pass the arguments!!!".center(75)+'\n')
    print('*'*75)

def search_ri():
    try:
        os.system('cls')
        res= os.walk(args.ri[1])
        dict1 ={}
        for r,d,f in res:
            for i in f:
                dict1.setdefault(i,[]).append(r)
        f = open("firstdata.txt","w")
        for k,v in dict1.items():
            for file in v:
                a = file+"\\"+k+"\n"
                f.write(a)
        f.close()
        
        f = open("firstdata.txt","r")
        data = f.readlines()
        print("Data Found:\n")
        file_check = 0
        file_count = 0
        for i in data:
            a = i.split("\n")[0]
            fr = open(a,'r')
            count = 0
            for line in fr:
                m = re.search(pattern, line,re.I)
                if m:
                    print(f'{m.group()} found in "{a}" >>>> at line number {count}')
                    file_count = file_count + 1            
                count = count + 1
            file_check = file_check + 1
        print(f'\nTotal files checked: {file_check} & Total Matches found: {file_count}.')
    except:
        err()
        
def search_si():
    try:
        os.system('cls')
        data = []
        path = args.si[1]
        for file in os.listdir(path):
            if os.path.isfile(path+"/"+file):
                data.append(file)
        f = open("firstdata1.txt","w")
        for file in data:
            a = path+"\\"+file+"\n"
            f.write(a)
        f.close()
        
        f = open("firstdata1.txt","r")
        data = f.readlines()
        print("Data Found:\n")
        file_check = 0
        file_count = 0
        for i in data:
            a = i.split("\n")[0]
            fr = open(a,'r')
            count = 0
            for line in fr:
                m = re.search(pattern, line,re.I)
                if m:
                    print(f'{m.group()} found in "{a}" >>>> at line number {count}')
                    file_count = file_count + 1            
                count = count + 1
            file_check = file_check + 1
        print(f'Total files checked: {file_check} & Total Matches found: {file_count}.')        
    except:
        err()
	
if args.ri:
    a = args.ri[0]
    pattern = a+'.*'
    search_ri()
elif args.si:
    a = args.si[0]
    pattern = a+'.*'
    search_si()
else:
    err()