from multiprocessing import Process
import random
import time

time_i = time.time()

def function(max_count):
	count = 0
	c_count = 0
	size = 0.5	
	size = float(size)

	while count < max_count:

		x = random.random()
		y = random.random()
	
		xp = x - size 
		yp = y - size

		rr = xp*xp + yp*yp

		if rr <= size*size:
			c_count+=1

		count+=1

	pi = 4*float(c_count)/max_count

	print "PI is %f" %pi;

if __name__ == 'main':
	p = Process(target=function, args=(1e10,))
	p.start()
	p.join

	p



		
