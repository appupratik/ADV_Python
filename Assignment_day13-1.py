from configparser import ConfigParser
import socket

print(socket.gethostbyname_ex(socket.gethostname())[-1])

config = ConfigParser()
config.read('ext.ini')

http_ip = config.get('HTTP','ip')
http_port = config.getint('HTTP','port')

print('HTTP IP'.ljust(10),http_ip.ljust(13))
print('HTTP PORT'.ljust(10),str(http_port).ljust(13), type(http_port))