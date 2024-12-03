file = 'C:/Users/Kiiya/Documents/GitHub/aoc2024/Day 1/input.txt'

leftValues = []
rightValues = []

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

def similarityScore():
    score = 0
    for leftValue in leftValues:
        times = 0
        for rightValue in rightValues: 
            if leftValue == rightValue: times += 1
        score += leftValue*times
    return score

initializeInput(file)
print(similarityScore())