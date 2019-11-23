#!/usr/bin/python

import random

A=[0,0]
B=[0,0]
C=0
pool=[-1.5,-1.0,-0.5,0.0,0.5,1.0,1.5]

for i in range(10000):
	A[0] += random.choice(pool)
	A[1] += random.choice(pool)
	B[0] += random.choice(pool)
	B[1] += random.choice(pool)
	
	if 0<abs((A[0]-B[0])-(A[1]-B[1]))<1:
		A[0]=B[0]=((A[0]+B[0])/2)+0.25
		A[1]=B[1]=((A[1]+B[1])/2)+0.25
		C +=1
	print('a',A[0],A[1],C)
	print('b',B[0],B[1],C)
	C -=1
