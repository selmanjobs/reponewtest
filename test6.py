#!/usr/bin/env python
#-*-coding:utf-8 -*-
expression = raw_input("p ve q değişkenleriyle tanımlanmış herhangi bir boolean ifade giriniz : ")

def truth_table (expression):
	print " p q %s" % expression
	length = len(" p q %s" % expression)
	print length*"="
	for p in True, False:
		for q in True, False:
			print "%-7s %-7s %-7s" % (p, q, eval(expression))
