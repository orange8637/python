#! /usr/bin/env python
# encoding: utf-8
from socket import *

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
	data = raw_input('>>> ')
	tcpCliSock.send(data)
	data = tcpCliSock.recv(BUFSIZE)
	print data
tcpCliSock.close()
