def getSublists(L, n):
	lst = []

	def recSubList(lst,L,n):
		slist =[]

		for i in range(0,n):
			slist.append(L[i])

		lst.append(slist)
		return recSubList(lst,L[1:],n)

	try:
		recSubList(lst, L, n)

	except IndexError,e:
		return lst
			



L = [1, 1, 1, 1, 4]

print getSublists(L, )