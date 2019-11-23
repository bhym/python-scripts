#!/usr/bin/python

import string
import random

string_pool = string.ascii_lowercase +' '+string.punctuation
phrase = list('a cat is a cat is not a cat')
b = []

random_string=list(''.join(random.choice(string_pool) for i in range(len(phrase))))
A = list(zip(phrase,random_string))
for i in range(0,len(A)):
	b.append(A[i][1])
pool = list(range(0,len(phrase)))

while phrase != random_string and len(pool) !=0:
	index = random.choice(pool)
	b[index] = random.choice(string_pool)
	if b[index] == phrase[index]:
		pool.remove(index)
	print(b)
