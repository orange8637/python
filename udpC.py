#! /usr/bin/env python
# encoding: utf-8
from socket import *

HOST = '192.168.1.105'
PORT = 2222
ADDR = (HOST, PORT)
BUFSIZE = 1024
udpCliSock = socket(AF_INET, SOCK_DGRAM)
while 1:
	data = raw_input('>> ')
	udpCliSock.sendto(data, ADDR)
	data, ADDR = udpCliSock.recvfrom(BUFSIZE)
	print data
udpCliSock.close()

