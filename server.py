import socket
import sys
import DES2
import DES
import random
from math import *
server_address = ('', 11001)
print >> sys.stderr, 'starting up on %s port %s' % server_address

q = 353
a = 3
xa = input("Random key : ")
YA = (a ** xa) % q
print YA
YA1 = str(YA)

# Listen for incoming connections
while True:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(server_address)
    sock.listen(1)

    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    connection.sendall(YA1)
    try:
        data=connection.recv(400)
        # print data
        num = 0
        KEYB = (int(data) ** xa) % q
        keyB = str (KEYB)
        i=len(keyB)
        j=0
        if len(keyB) < 8 :
            for i in range(len(keyB), 8):
                i+=1
                j+=1
                keyB = keyB + str(j)
        print keyB
        print >>sys.stderr, 'connection from', client_address
        # Receive the data in small chunks and retransmit it
        while True:
            # q = 353
            # a = 3
            # xa = random.randint(0,354)
            # xb = random.randint(0,354)
            # xaxb = "%d %d" % (xa, xb)
            # print xa, xb
            # connection.send(xaxb)
            # YA = (pow(a,xa)) % q
            # ya = "%d" % (YA)
            # connection.send(ya)
            # YB = sock.recv(1024)
            # KAB = (pow(YB,xb)) % q
            # print KAB
            # strKAB = str(KAB)
            # num = 0
            # if len(strKAB) < 8 :
            #     for i in range(len(strKAB), 8):
            #         strKAB[i] = num
            #         num+=1
            # k = strKAB
            data = connection.recv(16)
            with open ('terima.txt','wb') as c:
                data = c.write(data)
            execfile("DES2.py") 
            with open ('dekrip.txt','rb') as c:
                data = c.read()
            print >>sys.stderr, 'received "%s"' % data
            if data:
                message = raw_input('ngomong2 : ')
                with open ('hasil.txt','wb') as c:
                    data = c.write(message)
                execfile("DES.py")
                with open ('enkrip.txt','rb') as krm:
                    data2 = krm.read()
                print >> sys.stderr, 'sending "%s"' % message
                #print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data2)
            else:
                print >>sys.stderr, 'no more data from', client_address
            break
    finally:
        # Clean up the connection
        connection.close()