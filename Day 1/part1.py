file = 'C:/Users/Kiiya/Documents/GitHub/aoc2024/Day 1/input.txt'

leftValues = []
rightValues = []

distances = []

## Read the input file containing left and right values
def initializeInput(file):
    with open(file, 'r') as f:
        values = f.read().splitlines()
        for val in values:
            numbers = val.split("   ")
            left = numbers[0]
            right = numbers[1]
            leftValues.append(int(left))
            rightValues.append(int(right))

## Filter the values from smallest to biggest value
def sortValues():
    leftValues.sort()
    rightValues.sort()

## Get the distances
def getDistances():
    if not leftValues.__len__() == rightValues.__len__():
        print("Cannot measure distance between left and right values!")
        return
    for i in range(leftValues.__len__()):
        leftValue = leftValues[i]
        rightValue = rightValues[i]
        distance = abs(leftValue-rightValue)
        distances.append(distance)


## Final distance value
def getTotalDistance():
    finalValue = 0
    for distance in distances:
        finalValue = finalValue + distance
    return finalValue


initializeInput(file)
sortValues()
getDistances()
print("Total distance: " + str(getTotalDistance()))
