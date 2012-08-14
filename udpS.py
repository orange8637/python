#! /usr/bin/env python
# encoding: utf-8
from socket import *
from time import ctime

HOST = ''
PORT = 2222
BUFSIZE = 1024
ADDR = (HOST, PORT)
udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)
while True:
	data, addr = udpSerSock.recvfrom(BUFSIZE)
	udpSerSock.sendto('[%s] %s' %(ctime(), data), addr)
	print 'sendto ...%s' %(addr)
udpSerSock.close()
