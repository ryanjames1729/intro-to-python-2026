# We will have 3 doors: 1 door is the winner
# The contestant picks one door, then the host opens a different door
# The contestant should change their option
# We reveal if the contestant the right door
import random

def doorSimulation():
    winningDoor = random.randint(1,3)  #picks a random number [1,3]
    contestChoice = random.randint(1,3)

    #print("Winner: " + str(winningDoor) + "; Contestant Choice: " + str(contestChoice))

    revealDoor = random.randint(1,3)
    while revealDoor == winningDoor or revealDoor == contestChoice:
        revealDoor = random.randint(1,3)

    #print("Winner: " + str(winningDoor) + "; Contestant Choice: " + str(contestChoice) + "; Host Opens Door #" + str(revealDoor))

    contestFinal = random.randint(1,3)
    while contestFinal == contestChoice or contestFinal == revealDoor:
        contestFinal = random.randint(1,3)

    winner = False
    if contestFinal == winningDoor:
        #print("The contestant wins a brand new car!")
        winner = True
    
    return winner

countOfWins = 0
numberOfSimulations = 10000000000
for i in range(numberOfSimulations):
    win = doorSimulation()
    if i % 100 == 0:
        print("Simulation #" + str(i) + " running...")
    if win:
        countOfWins += 1

print("\n\nOut of " + str(numberOfSimulations) + " simulations, you won " + str(countOfWins) + " times.")
