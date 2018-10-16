#!/bin/env python
#! coding utf-8
import sys
import re
from collections import OrderedDict

with open('mask.txt', mode='r') as f:
	lines = f.readlines()
	masklist = OrderedDict()
	for l in lines:
		m = re.search(r'^(\w+)\t(.*)$', l)
		if m:
			if not(m.group(1) in masklist):
				masklist[m.group(1)] = []
			masklist[m.group(1)].append(m.group(2))
	for cc in masklist:
		num = 0
		for v in masklist[cc]:
			print("object network country-%s-%05d"%(cc,num))
			m = re.search(r'([0-9.]+)/([0-9.]+)$', v)
			print(" subnet %s %s"%(m.group(1), m.group(2)))
			num += 1
		print("object-group network country-group-%s"%cc)
		for i in range(num):
			print(" network-object object country-%s-%05d"%(cc, i))
