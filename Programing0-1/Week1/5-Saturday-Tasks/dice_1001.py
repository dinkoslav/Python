mariika_points = 1001
ivancho_points = 1001
game_is_over = False
mariika_turn = True

from random import randrange

while game_is_over == False:
    if mariika_turn == True and game_is_over == False:
        firstRoll = randrange(1,6)
        secondRoll = randrange(1,6)
        thirdRoll = randrange(1,6)
        fourthRoll = randrange(1,6)
        fifthRoll = randrange(1,6)
        sum = firstRoll + secondRoll + thirdRoll + fourthRoll + fifthRoll
        numbers = str(firstRoll) + ", " + str(secondRoll) + ", " + str(thirdRoll) + ", " + str(fourthRoll) + ", " + str(fifthRoll)
        print("Mariika roll " + numbers + ", sum is: " + str(sum))
        if mariika_points > 0:
            mariika_points = mariika_points - sum
        else:
            mariika_points = mariika_points + sum
        if mariika_points == 0:
            game_is_over = True
            mariika_win = True
            break
        print("Mariika points left: " + str(mariika_points))
        mariika_turn = False
    if mariika_turn == False and game_is_over == False:
        firstRoll = randrange(1,6)
        secondRoll = randrange(1,6)
        thirdRoll = randrange(1,6)
        fourthRoll = randrange(1,6)
        fifthRoll = randrange(1,6)
        sum = firstRoll + secondRoll + thirdRoll + fourthRoll + fifthRoll
        numbers = str(firstRoll) + ", " + str(secondRoll) + ", " + str(thirdRoll) + ", " + str(fourthRoll) + ", " + str(fifthRoll)
        print("Ivancho roll " + numbers + ", sum is: " + str(sum))
        if ivancho_points > 0:
            ivancho_points = ivancho_points - sum
        else:
            ivancho_points = ivancho_points + sum
        if ivancho_points == 0:
            game_is_over = True
            mariika_win = False
            break
        print("Ivancho points left: " + str(ivancho_points))
        mariika_turn = True
        
print("Mariika points: " + str(mariika_points))
print("Ivancho points: " + str(ivancho_points))
if mariika_win == True:
    print("Mariika wins!")
else:
    print("Ivancho wins!")




          
