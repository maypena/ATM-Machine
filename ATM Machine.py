# May Pena
# This program asks the user for some amount of dollars and outputs
# the dollar bills that should be distributed
# user inputs

userWith = int( abs( eval( input ("Please enter the amount to withdraw: ") ) ) )

print ()

# box
print("+--------------------------------+")
print("| Withdrawal amount: ${0:<11}| ".format(userWith))

# computation
no20s    = userWith // 20
userWith = userWith % 20
no10s    = userWith // 10
userWith = userWith % 10
no5s     = userWith // 5
userWith = userWith % 5
no1s     = userWith // 1

# outputs
print   ("| $20-bill(s): {0:<18}|".format(no20s))
print   ("| $10-bill(s): {0:<18}|".format(no10s))
print   ("| $5-bill(s):  {0:<18}|".format(no5s))
print   ("| $1-bill(s):  {0:<18}|".format(no1s))
print   ("+--------------------------------+")
