#!/usr/bin/python
#import sys
import turtle as t
#import random as r
def move(Y):
	t.up()
	t.right(90)
	t.forward(Y)
	t.left(90)
	t.down()
	return

#a = sys.argv
t.reset()
t.colormode(255)
#col= (189,183,107),(189,183,107),(240,230,140),(238,232,170),(238,232,170),(250,250,210),(250,250,210),(255,255,224),(255,255,224),(238,221,130),(238,221,130),(218,165,32),(184,134,11),(184,134,011),(139,69,19),(139,69,19),(160,82,45),(205,133,63),(222,184,135),(245,245,220),(245,222,179)
rings = [(12,2),(34,5),(2,1),(1,1),(45,7),(30,4),(56,2),(70,8),(10,1),(10,1),(10,1),(10,1)] 
x = 0
#k = int(a[1])
k = 10
#while k>10:
#for i in range(int(a[1])):
for i in rings:
		k += x  
		t.ht()	
		t.color((210,180,140))
		t.pensize(i[1])
		t.circle(k)
		#m = r.choice(range(10))
		#move(m)
		move(i[0])
		x = i[0]

t.exitonclick()

