
class Staff:
    def __init__(self, pPosition, pName, pPay):
        self._position = pPosition
        self.name = pName
        self.pay = pPay
        print('Creating Staff object')

    def __str__(self):
        return 'Position = %s, Name = %s, Pay = %d' %(self._position, self.name, self.pay)

    def calculatepay(self):
        prompt = '\n Enter numbers hours worked for %s:' %(self.name)
        hours = input (prompt)
        prompt = '\n Enter hourly rate for %s:' %(self.name)
        hourlyRate = input (prompt)
        self.pay = int(hours)*int(hourlyRate)
        return self.pay

    @property
    def position(self):
        print("Getter Method")
        return self._position

    @position.setter
    def position(self, value):
        if value == 'Manager' or value == 'Basic':
            self._position = value
        else:
            print('Position is invalid. No changes made.')



Rob = Staff('dev' , 'Robert', 37000)
Rob.position = 'Manager'
# print(Rob.position)

class A:
    def __init__(self):
        self.__x = 5
        self._y = 6

varA = A()
print(varA._y)
print(varA.__x)