from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
from directKeys import PressKey, ReleaseKey, W, A
import time

PORT_NUMBER = 5000
SIZE = 1024

hostName = gethostbyname( '192.168.1.125' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print("Test server listening on port {0}\n".format(PORT_NUMBER))

while True:
        (data,addr) = mySocket.recvfrom(SIZE)
        meme = data.decode('utf-8')
        print(meme)
        if meme == 'On':
                PressKey(W)
                time.sleep(1)
                ReleaseKey(W)
        else:
                ReleaseKey(W)
                
sys.ext()
