#!/usr/bin/python

import random
import string

def gen():
	A=[0,0,0,0,0,0,0,0,0]
	for i in range(len(A)): A[i]=random.randint(0,25)
	return A

def fen(X):	
	B=[]
	for i in range(len(X)):
		if X[i] != 0 : B.append(string.ascii_lowercase[X[i]])
	B=''.join(B);
	return B

def selection(X):
	voc=0.00
	con=0.00
	vot=0.00
	cot=0.00
	for i in range(len(X)):
		if X[i] in "aeiou": voc +=1.0
		else: con +=1.0
		vot=(10.0 * voc) / (voc+con)
		cot= 10.0 - vot
		if vot == 0 : vot = 1.0 
		sieve = 1.7<cot/vot<2.7
	if sieve  is False : 
		C[0] = "Die"
	else: 
		C[0] = "Survive"
	return 

def reproduction(y,x):	
	if (x and y != []) and (len(x[1]) == len(y[1])):
		son[0]=[0 for k in range(len(x[0]))]
		for j in range(len(x[0])) : son[0][j] = int((x[0][j]+y[0][j])/2)
		son[1] = fen(son[0])
		print("mum", x)
		print("dad", y)
		print("son", son)
		print("---------------------------------")
	else:
		print("No breeding")
		print("---------------------------------")
	x=[]
	y=[]
	return

population=[]
cemetery=[]
breeding=[]
C=[0]
dad=[]
mum=[]
son=[0,[]]
for i in range(1000) :
	tmp= gen()
	population.append((tmp,fen(tmp)))
	selection(population[i][1])
	if C[0] is "Die" : cemetery.append(population[i])
	elif C[0] is "Survive" :  breeding.append(population[i])

for i in range(10):
	chance = 27 < random.randint(0,len(breeding)) < 37
	if chance is True: 
		bm= random.randint(0,len(breeding)-1)
		bd= random.randint(0,len(breeding)-1)
		mum = breeding[bm]
		dad = breeding[bd]
		reproduction(mum,dad)
