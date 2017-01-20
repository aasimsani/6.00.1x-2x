balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

MIR = annualInterestRate/12.0

months = 12
TP = 0
for i in range(1,months+1):
	if i < months:
		MP = balance*monthlyPaymentRate
		UpB= balance - MP
		Int = MIR*UpB
		TP += MP
		balance = Int + UpB
		print "Months:", i 
		print "Minimum monthly Payment:",("%.2f" % MP)
		print "Remaining balance:", ("%.2f" % balance)
	else:
		MP = balance*monthlyPaymentRate
		UpB= balance - MP
		Int = MIR*UpB
		TP += MP
		balance = Int + UpB
		print "Months:", i 
		print "Minimum monthly Payment:",("%.2f" % MP)
		print "Remaining balance:", ("%.2f" % balance)
		print "Total paid:", ("%.2f" % TP)
		print "Remaining balance:", ("%.2f" % balance)

