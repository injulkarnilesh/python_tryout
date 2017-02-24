import random
difficultyLevel = random.randint(1,5)
newPower = int(random.randint(10, 50)/difficultyLevel)
currentPower = 50
currentPower += newPower
print(difficultyLevel, ">" , currentPower)
