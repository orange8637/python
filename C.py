#! /usr/bin/env python
# encoding: utf-8
from socket import *

ADDR = ('192.168.1.103', 2222)
C = socket(AF_INET, SOCK_STREAM)
C.connect(ADDR)

while True:
	data = raw_input(">>> ")
	C.send(data, ADDR)
	data = C.recv(1024)
	print data
