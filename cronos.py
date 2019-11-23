#!/usr/bin/python

import random

pop = [['f',9,'o',0] for i in range(50)] + [['f',9,'e',0] for i in range(50)] 
res = [random.randint(2,99) for i in range(5000)]
carcass = []
respiration_time = 0
reproduction_time = 0
decomposition_time = 0
cicle = 0
#sprouting_time=0
#soil = []
#plantulae = []

print("cycle","res","pop","carc")
while len(res) !=0 and len(pop) !=0:

	if len(res) > len(pop): encounters= zip(pop,random.sample(res,len(pop)))
	else: encounters = zip(random.sample(pop,len(res)),res)
	for i,prey in encounters:
		if prey%2 == 0 and i[2] == 'e' :
			digested = abs(int((prey/2)-1))
			if digested >= 1: res.append(digested)
			i[1] +=9
			res.remove(prey)
		if i[2] == 'o' and prey%2 != 0 and prey !=1 :
			digested = abs(int(prey/2)-(int(prey/2)%2))
			if digested >=1: res.append(digested)
			i[1] +=9
			res.remove(prey)

	if respiration_time==10 :
		for elem in pop :
			if elem[1] > 0: elem[1]-=6
		respiration_time=0

	for i in pop:
		i[3] +=1
		if i[1] <= 0 or i[3] == 65: carcass.append(i) ; pop.remove(i)
		
	for j in res:
		if j ==1: res.remove(j)
		#	soil.append(j)
		elif j == 0: res.remove(j)

	if decomposition_time==20:
		for i in carcass:
			decompose=abs(int(i[1]/3))
			if decompose > 1: 
				res.append(decompose)
			carcass.remove(i)
		decomposition_time=0

	#if sprouting_time == 17+random.randint(0,10):
	#	sprouts=random.sample(soil, random.randint(0,len(soil)))
	#	for i in sprouts: 
	#		plantulae.append(2)
	#		soil.remove(i)

	if reproduction_time == 20+random.randint(-10,10):
		repr_pool=random.sample(pop, int(len(pop)/2))
		for elem in repr_pool:
			if elem[1] > 75: pop[len(pop):]=[[cicle,abs(int((elem[1]/2)-12)),elem[2],0]]
		reproduction_time = 0
		
	cicle +=1
	reproduction_time +=1
	decomposition_time +=1
	respiration_time +=1
	#sprouting_time +=1
	#for i in plantulae: i +=1
	
	#for i in random.sample(plantulae,random.randint(0,len(plantulae))):
	#	res.append(i)
	#	plantulae.remove(i)

	print (cicle,len(res),len(pop),len(carcass))

#if len(res) == 0: print ("Risorse esaurite dopo",cicle,"cicli\n")
#if len(pop) == 0: print("Popolazione estinta dopo",cicle,"cicli\n")


