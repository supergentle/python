import multiprocessing

def worker():
	print 'worker'
	return

size = 1e6
size = int(size)

if __name__ == '__main__':

	jobs = []
	for i in range(size):
		p = multiprocessing.Process(target=worker)
		jobs.append(p)
		p.start()
		p.join()
