#! /usr/bin/env python
# encoding: utf-8
from socket import *

S = socket(AF_INET, SOCK_STREAM)
ADDR = ('', 2222)
S.bind(ADDR)
S.listen(1)

while True:
	C, addr = S.accept()
	print 'connected from',addr
	while True:
		data = C.recv(1024)
		print data
		data = raw_input('>>> ')
		C.send(data, addr)
	C.close()
S.close()
