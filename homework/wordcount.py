"""
	Ronald Uy & Edwin Cheung
	CMSI 386 Homework 1 - Dr. Toal
"""

import sys
wordcount={}

for line in sys.stdin:
	line = ''.join(line)
	line = line.lower()
	line = line.split(" ")

	for i in range (0,len(line)):
		line[i]=[c for c in line[i].decode('unicode_escape') if 97<=ord(c)<=122 or ord(c)==39]
		line[i] = str(''.join(line[i]))
	line.sort()
	
	for word in line:
		if word not in wordcount:
			wordcount[word] = 1
		else:
			wordcount[word] += 1

store=[]
for key in wordcount.keys():
	store.append(key)
store.sort()

for key in store:
		if not key == '':
			print ("%s %s " %(key , wordcount[key]))
