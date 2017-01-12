def genPrime():
	last = 1
	Primes = []
	while True:
		last += 1
		for p in Primes:
			if last % p == 0:
				break
		else:
			Primes.append(last)
			yield last

c = genPrime()

for i in range(0,10):
	print c.next()
