import os
from configparser import ConfigParser

config = ConfigParser()
config.read('ext1.ini')

print("==>",os.getcwd())
os.chdir(config.get('EXT','current_path'))
print("==>",os.getcwd())

for i in os.listdir("."):
    if i.endswith(config.get('EXT','from')):
        #print(i)
        first_name = i.rsplit(".",1)[0]
        j=first_name+"."+config.get('EXT','to')
        os.rename(i,j)