balance = 999999
annualInterestRate = 0.18

current_balance = balance
MIR = annualInterestRate/12.0

MinPM = 0

lowerbound = balance/12
upperbound = (balance*((1+MIR)**12))/12.0

while (abs(current_balance) > 0.01):
	current_balance = balance
	MinPM = (lowerbound+upperbound)/2
	for i in range(12):
		UpB = current_balance - MinPM
		current_balance = UpB + (UpB*MIR)
	if current_balance > 0:
		lowerbound = MinPM
	elif current_balance < 0:
		upperbound = MinPM
	
	

print ("%.2f" % MinPM)


