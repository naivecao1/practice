#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Co,.Ltd:Lcmj, programe:practice'

__author__ = 'naivecao'


# Function programe
def abc(x):
	return x * x

def abd(x, y, abc):
	return abc(x) + abc(y)

#print abd(3, 4, abc)
# Function programe map/reduce
#print map(abc, [1, 2, 3])
def fn(x, y):
	return x * 10+ y
	
print reduce(fn, [1, 3, 5, 7, 9])