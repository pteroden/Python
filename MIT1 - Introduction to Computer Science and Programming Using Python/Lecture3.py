'''
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

balance = 320000
annualInterestRate = 0.2

updatedBalance = balance
monthlyUnpaidBalance = balance
lower = balance/12.0
higher = (balance * (1 + annualInterestRate/12.0)**12) / 12.0
epsilon = 0.01


while abs(updatedBalance) > epsilon:
    minimum = (lower + higher)/2.0
    updatedBalance = balance
    for month in range(1, 13):
        monthlyUnpaidBalance = updatedBalance - minimum
        updatedBalance = monthlyUnpaidBalance + (annualInterestRate/12.0 * monthlyUnpaidBalance)
        # print 'Monthly unpaid: ' + str(round(monthlyUnpaidBalance, 2)) + ', Updated: ' + str(round(updatedBalance,2)) + ', Minimum: ' + str(round(minimum, 2))
    if monthlyUnpaidBalance > 0:
        lower = minimum
    else:
        higher = minimum

print 'Lowest Payment: ' + str(round(minimum, 2))





# updatedBalance = balance
# monthlyInterestRate = (annualInterestRate) / 12
# epsilon = 0.01
# numGuesses = 0
# lowerBound = balance / 12
# upperBound = (balance * (1 + monthlyInterestRate)**12) / 12
# ans = (upperBound + lowerBound)/2.0
#
# while abs(0-updatedBalance) >= epsilon:
#     updatedBalance = balance
#     numGuesses += 1
#     for i in range(0,12):
#         updatedBalance = round(((updatedBalance - ans) * (1 + monthlyInterestRate)), 2)
#         if updatedBalance >= 0:
#             lowerBound = ans
#         else:
#             upperBound = ans
#         ans = (upperBound + lowerBound)/2.0
# print "Lowest Payment: " + str(round(ans, 2))