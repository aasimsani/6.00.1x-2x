def clip(lo,x,hi):
	return min(hi,(max(lo,x))) 



print clip(2,4,3)