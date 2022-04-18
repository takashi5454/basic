#if文
balance =1000
 withdraw =105
 upper_limit=100

if balance > withdraw and upper_limit >= withdraw:
    balance = balance-withdraw
    print("your new balance is {}".format(balance))
else:
    print("no handing")