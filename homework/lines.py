"""
	Ronald Uy & Edwin Cheung
	CMSI 386 Homework 1 - Dr. Toal
"""

import sys
with open(sys.argv[1]) as f:
	count=0
	symbol=0
	for line in f:
		num_lines = sum(1 for line in f if line.strip('\n'))
	if line.strip('#'):
		symbol+=1
	if len(line)-len(line.strip())>0 :
		count+=1
	num_lines=num_lines-symbol-count
	print num_lines
f.close()
