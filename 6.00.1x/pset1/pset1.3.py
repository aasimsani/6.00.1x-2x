

st = s[0]
en = s[0]

for i in range(1,len(s)):
	if s[i] >= st[-1]:
		st += s[i]
		if len(st) > len(en):
			en = st

	else:
		st = s[i]

print "Longest substring in alphabetical order is",  en

