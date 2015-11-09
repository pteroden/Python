# coding=utf-8
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
paid = 0


for month in range(1, 13):
    minMonthPay = balance * monthlyPaymentRate
    paid += minMonthPay
    balance -= minMonthPay
    balance *= 1 + annualInterestRate/12
    print 'Month: ' + str(month)
    print 'Minimum monthly payment: ' + str(round(minMonthPay, 2))
    print 'Remaining balance: ' + str(round(balance, 2))

print 'Total paid: ' + str(round(paid, 2))
print 'Remaining balance: ' + str(round(balance, 2))