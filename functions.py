def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if (numberToCheck%x == 0):
            return False

    return True

# print(checkIfPrime(4))


n = 2

print('the number is %s' %n)





