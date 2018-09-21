# Python program to implement client side of chat room. 
import socket 
import select 
import sys 
from Crypto.Cipher import AES
import base64

key = raw_input("What is the key?")
if len(key) < 16:
    counter = 0
    while len(key) != 16:
        counter += 1
        key += str(counter)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
    print "Correct usage: script, IP address, port number"
    exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port))

def encrypt(privateInfo, key):
    BlockSize = 16
    padding = '{'

    pad = lambda s: s + (BlockSize - len(s) % BlockSize) * padding

    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))

    
    #print "Encryption Key: ", key

    cipher = AES.new(key)
    #print cipher

    encoded = EncodeAES(cipher, privateInfo)
    #print "Encrypted String: ", encoded
    return encoded

def decrypt(encryptedString, key):
    padding = '{'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(padding)
    cipher = AES.new(key)
    decoded = DecodeAES(cipher, encryptedString)
    #print decoded
    return decoded 
  
while True: 
  
    # maintains a list of possible input streams 
    sockets_list = [sys.stdin, server] 
  
    """ There are two possible input situations. Either the 
    user wants to give  manual input to send to other people, 
    or the server is sending a message  to be printed on the 
    screen. Select returns from sockets_list, the stream that 
    is reader for input. So for example, if the server wants 
    to send a message, then the if condition will hold true 
    below.If the user wants to send a message, the else 
    condition will evaluate as true"""
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 
  
    for socks in read_sockets: 
        if socks == server: 
            message = socks.recv(2048) 
            if message == "Welcome to this chatroom!":
                print message
            else:
                #print message[message.index(" ")+1:]
                print message[:message.index(" ")+1],decrypt(message[message.index(" ")+1:], key)
        else: 
            message = sys.stdin.readline() 
            server.send(encrypt(message, key))
            sys.stdout.write("<You>") 
            sys.stdout.write(message) 
            sys.stdout.flush() 
server.close() 