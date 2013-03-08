#! /usr/bin/env python
# encoding: utf-8

import sys

def fib(n):
	if n < 2:
		return 1
	return fib(n-2) + fib(n-1)

print fib(int(sys.argv[1]))
