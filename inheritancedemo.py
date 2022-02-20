import classdemo

peter = classdemo.BasicStaff('Peter', 0)
john = classdemo.ManagementStaff('John', 0, 1000, 0)

print(peter)
print(john)

print('Peter\'s pay = ', peter.calculatepay())
print('John\'s pay = ', peter.calculatepay())

# print('Peters\'s Performance Bonus = ', peter.calculatePerfBonus())
print('John\'s Performance Bonus = ', john.calculatePerfBonus())

totalPay = john + peter
print('\nTotal Pau for Both Staff = ', totalPay)