import time
from joblib import Parallel, delayed
import multiprocessing
#primes

class prime:
	def printPrime(end):

		start_time = time.time()

		primesL = []

		for num in range(1, int(end)):
			isprime = True
			for i in range(2, num):
				if(num % i == 0):
					isprime = False
			if(isprime):
				primesL.append(num)

		end_time = time.time() - start_time

		print(primesL)

		print("\nExecution time: ", " %s seconds" %(end_time))
"""
	def printPrimeParallel(end):

		start_time = time.time()
		inputs = range(1, end)
		num_cores = multiprocessing.cpu_count()

		results = Parallel(n_jobs=num_cores)(delayed(processPrime)(i) for i in inputs)

		end_time = time.time() - start_time

		print(results)

		print("\nExecution time: ", " %s seconds" %(end_time))

	def processPrime(num):
		isprime = True
		for i in range(2, num):
			if(num % i == 0):
				isprime = False
		if(isprime):
			return num
"""
	#borrowed solution for comparison
	def get_primes(n):

    	numbers = set(range(n, 1, -1))
    	primes = []
    	while numbers:
    		p = numbers.pop()
        	primes.append(p)
        	numbers.difference_update(set(range(p*2, n+1, p)))

    	return primes


	def initialise():
		max = input("max value: ")

		#prime.printPrime(max)
		#prime.printPrimeParallel(max)
		prime.get_primes(max)

prime.initialise()


