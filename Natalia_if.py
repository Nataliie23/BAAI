
#
# Natalia
# Short description of the task
#

# 1. Input
account_balance = 5000
withdrawal = 6000
# 2. Process
if withdrawal <= account_balance:
    account_balance -= withdrawal
    print("withdrawal sucessful. New balance: $¨{account_balance}")
else:
    print("Insufficient funds!")
# 3. Output
 