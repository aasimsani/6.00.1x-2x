def gcditer(a, b):
	gcd = min(a,b)
	while a % gcd != 0 or b % gcd != 0:
		gcd -=1

	print gcd 
