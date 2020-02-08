import socket
import time



HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Af_Inet correspond to ipv4 and sock_stream correspond to tcp
s.bind(("192.168.8.82", 1244))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established")

    msg=input("Please enter your message: ")
    #msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg 

    clientsocket.send(bytes(msg, "utf-8"))

   #while True:
        #time.sleep(3)
        #msg = f"The time is ! {time.time()}"
        #msg = f'{len(msg):<{HEADERSIZE}}' + msg
        #clientsocket.send(bytes(msg, "utf-8")) '''
    


