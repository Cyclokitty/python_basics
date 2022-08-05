import random

def getAnswer(answerNum):
    if answerNum == 1:
        return 'It is certain.'
    elif answerNum == 2:
        return 'It is decidedly so.'
    elif answerNum == 3:
        return 'Yes'
    elif answerNum == 4:
        return 'No'
    elif answerNum == 5:
        return 'It is unacceptable'
    elif answerNum == 6:
        return 'It is very doubtful'

r = random.randint(1, 6)
diceRoll = getAnswer(r)
print(diceRoll)