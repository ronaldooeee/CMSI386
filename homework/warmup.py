"""
Ronald Uy & Edwin Cheung
CMSI 386 Homework 1 - Dr. Toal
"""
from random import shuffle
import sys, struct

def change(x):
	if x >= 0: 
		quarters=divmod(x,25)
		dimes=divmod(quarters[1],10)
		nickels=divmod(dimes[1],5)
		pennies=divmod(nickels[1],1)
		if pennies[1]<1:
			print (quarters[0],dimes[0],nickels[0],nickels[1])
		else:
			print (quarters[0],dimes[0],nickels[0],pennies[0])
	else :
				raise ValueError('amount cannot be negative')

def scramble(word):
	word = list(word)
	shuffle(word)
	return ''.join(word)


def strip_quotes(str):
	str = str.replace("\'","")
	str = str.replace("\"","")
	print str


def prefixes(str):
	p = str
	for i in range (0,len(p)+1):
		yield p[:i]
	
def powers_of_two(a):
	x = 1
	while x <= a:
		yield x
		x = x*2

def interleave(list1 = [], list2 = []):
	full = []
	for i in zip(list1,list2):
		full.extend(i)
	if len(list1)==len(list2):
		print full
	elif len(list1)>len(list2):
		keepgoing = full+list1[len(list2):]
		print keepgoing
	elif len(list2)>len(list1):
		keepgoing2 = full+list2[len(list1):]
		print keepgoing2

def stutter(list1 = []):
	result = []
	for i in zip(list1, list1):
		result.extend(i)
	print result
	
