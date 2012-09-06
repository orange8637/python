#! /usr/bin/env python
# encoding: utf-8

import os, sys


class mysql:
	def create(self):
		string = "create table student (name varchar(20), age int(2) );"
		f = file("a.sql", "w")
		res = "---name---age---\n"
		f.write(res)
		res = "   姜晨   20\n"
		f.write(res)
		res = "   马云   99\n"
		f.write(res)
		print string
		f.close()
	def select(self):
		string = "select * from student"
		f = file("a.sql")
		l = f.readline()
		while l:
			print l
			l = f.readline()
		print "\n %s" %(string)
		f.close()

m = mysql()
m.create()
m.select()




