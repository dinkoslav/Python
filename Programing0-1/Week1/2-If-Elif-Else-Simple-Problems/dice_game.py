N = input("Enter sides: ")
from random import randrange
firstRoll = randrange(1,int(N))
secondRoll = randrange(1,int(N))
firstPlayerName = input("Enter player1 name: ")
secondPlayerName = input("Enter player2 name: ")
print (firstPlayerName + " roll " + str(firstRoll))
print (secondPlayerName + " roll " + str(secondRoll))
if firstRoll > secondRoll:
    print(firstPlayerName + " wins!")
elif firstRoll < secondRoll:
    print(secondPlayerName + " wins!")
else:
    print("Draw!")
