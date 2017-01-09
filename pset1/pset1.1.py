
s = 'azcbobobegghakl'
# No need to have s 
count = 0
lst =[]
for word in s:
	lst.append(word)

for e in lst:
	if e == "a":
		count += 1
	elif e == "e":
		count += 1
	elif e == "i":
		count += 1
	elif e == "o":
		count += 1
	elif e == "u":
		count += 1

print count 


		
