import socket
import sys
import DES
import DES2
import random
import math

q = 353
a = 3
xb = input("Random key : ")
YB = (a ** xb) % q
print YB
YB1 = str(YB)

while True:
    try:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 11001)
        #print >> sys.stderr, 'connecting to %s port %s' % server_address
        sock.connect(server_address)
        #key
        
        # data = sock.recv(1024)
        # data = data.split()
        # xa = data[0]
        # xb = data[1]
        # print xa, xb
        # #print a, q, xa, xb
        # YA = sock.recv(1024)
        hazil=sock.recv(50)
        print hazil
        KEYA = (int(hazil) ** xb) % q
        print KEYA
        sock.send(YB1)
        # KAB = (pow(YA,xa)) % q
        # print KAB
        # strKAB = str(KAB)
        # num = 0
        # if len(strKAB) < 8 :
        #     for i in range(len(strKAB), 8):
        #         strKAB[i] = num
        #         num+=1
        # k = strKAB
        # Send data
        message = raw_input('ngomong : ')
        with open ('hasil.txt','wb') as c:
            data = c.write(message)
        execfile("DES.py")
        with open ('enkrip.txt','rb') as krm:
            data2 = krm.read()
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(data2)
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(50)
            amount_received += len(data)
            with open ('terima.txt','wb') as c:
                data = c.write(data)
            execfile("DES2.py") 
            with open ('dekrip.txt','rb') as c:
                data = c.read()
            print >>sys.stderr, 'received "%s"' % data

    finally:
        sock.close()