#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Co,.Ltd:Lcmj, programe:practice'

__author__ = 'naivecao'


def abc(n):
	if n == 1:
		return n
	return n * abc(n - 1)


import os # 导入os模块，模块的概念后面讲到
print [d for d in os.listdir('.')] # os.listdir可以列出文件和目录