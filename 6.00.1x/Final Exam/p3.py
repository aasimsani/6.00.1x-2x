
d = {4:True, 3:True, 0:True}


def dict_invert(dic):

	retdic = {}

	for i in dic.keys():

		if dic[i] not in retdic.keys():
			retdic[dic[i]] = [i]

		elif dic[i] in retdic.keys():
			retdic[dic[i]].append(i)
			lst = retdic[dic[i]]
			lst.sort()
			retdic[dic[i]] = lst



	return retdic


print dict_invert(d)

