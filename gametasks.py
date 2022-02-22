import os

def printInstruction(instruction):
    print(instruction)

def getUserScore(userName):
        f = open('userScores.txt', 'r')
        for line in f:
            content = line.split(', ')
            if content[0] == userName:
                f.close()
                return(content[1])

        f.close()
        return "-1"

def updateUserScore(newUser, userName, score):
    if newUser == True:
        f = open('userScores.txt', 'a')
        f.write('\n%s, %s' %(userName, score))
        f.close()
    else:
        tmp = open('userScores.tmp', 'w')
        txt = open('userScores.txt', 'r')
        for line in txt:
            content = line.split(', ')
            if content[0] == userName:
                tmp.write('%s, %s\n' %(userName, score))
            else:
                tmp.write('%s, %s' %(content[0], content[1]))

        tmp.close()
        txt.close()

        os.remove('userScores.txt')
        os.rename('userScores.tmp', 'userScores.txt')
        


# print(getUserScore('Benny'))

# updateUserScore(True, 'BEN', 2)
updateUserScore(False, 'Ann', 100)