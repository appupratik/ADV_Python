import requests
import re
url = "https://study-ccna.com/classes-of-ip-addresses/"

collected_data = requests.get(url)
txt_data = collected_data.text
#print(txt_data)

ip = r'[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}'


ip_address = re.findall(ip,txt_data)
ip_address =list(set(ip_address))
i = 1
for each in ip_address:
    print(str(i).ljust(3),each)
    i = i + 1