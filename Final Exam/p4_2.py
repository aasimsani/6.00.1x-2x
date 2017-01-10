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


def longestRun(L):
	bestx = 0
	count = 0

	if len(L) == 1:
		return 1
	try:
		for i in range(0,len(L)):
			if L[0+i] < L[1+i] or L[0+i] == L[1+i]:
				count += 1

			elif L[0+i] > L[1+i] and bestx < count:
				bestx = count
				count = 0

	except IndexError,e: 
		if count > bestx:
			return count + 1 
		else:
			return bestx + 1

tcases = [[0],[1, 1, 1, 1, 1],[-10, -5, 0, 5, 10],[10, 4, 6, 8, 3, 4, 5, 7, 7, 2],[1, 2, 3, -1, -2, -3, -4, -5, -6],[-1, -2, -3, -4, -5, -6, -7, 2, 3],[1, 3, 5, -1, -3, -5, -7, 1, 3, 5],[10, 8, 9, 5, 6, 7, 1, 2, 3, 4],[14, 16, 18, 20, 8, 10, 12, 4, 6, 2],[7, 4, 1, -7, -11],[10, 4, 6, 8, 3, 3, 4, 5, 7, 7, 2, 9],[1, 0, 0, 0, 4, 5, 1, 2, 9, 4, -1, 0]]
answers = [1,5,5,5,3,3,4,4,4,1,6,5]

for i in tcases:
	if longestRun(i) == answers[tcases.index(i)]:
		print tcases.index(i),": Works"
	else:
		print tcases.index(i),": Not working. Answer: ", longestRun(i), "Expected: ",answers[tcases.index(i)]
		print i


