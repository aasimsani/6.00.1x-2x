balance = 3926
annualInterestRate = 0.2

'''
minFixedMonthlyPayment = balance / 12.0

monthlyInterestRate = annualInterestRate/12.0

c_bal = balance

while c_bal > 0:
	minFixedMonthlyPayment += 1
'''

current_balance = balance
MIR = annualInterestRate/12

MinPM = 0

add = 10

while (current_balance > 0):
	current_balance = balance
	MinPM += add
	for i in range(12):
		UpB = current_balance - MinPM
		current_balance = UpB + (UpB*MIR)

print "Lowest Payment: ",MinPM