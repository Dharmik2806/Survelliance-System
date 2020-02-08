import socket
from gtts import gTTS
import os
import pyttsx3

#from engine import engine

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1244))


while True:

    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        #if len(msg) <= 0:
            #break
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg.decode("utf-8")

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            #new_msg = True
            #full_msg = ''
            print(full_msg)

            engine = pyttsx3.init()
            engine.say(full_msg)
            engine.setProperty('rate',60)  #120 words per minute
            engine.setProperty('volume',0.9) 
            engine.runAndWait()

            

            
         