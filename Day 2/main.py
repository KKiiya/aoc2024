file = 'C:/Users/Kiiya/Documents/GitHub/aoc2024/Day 2/input.txt'

reports = []

## Read the input file containing left and right values
def initializeInput(file):
    with open(file, 'r') as f:
        fileReports = f.read().splitlines()
        for val in fileReports:
            valueAppended = []
            for i in val.split(" "):
                valueAppended.append(int(i))
            reports.append(valueAppended)

def isSafe(report):
    for i in range(len(report) - 1):
        diff = abs(report[i+1] - report[i])
        if diff not in [1, 2, 3]: return False
    return True

def checkSafeReports():
    safeReports = 0
    tempSafeReports = []
    for i in range(0, len(reports)):
        # print("Scanning repot Nº" + str(i))
        report = list(reports[i])
        firstReportValue = report[0]

        difference = report[0] - report[1]

        decreasing = False
        if difference > 0: decreasing = True
        # print(str(decreasing) + " " + str(report))

        safe = False
        for j in range(2, len(report)):
            if decreasing and firstReportValue >= report[j]: break
            elif (not decreasing) and firstReportValue <= report[j]: break
            safe = True
        if safe: tempSafeReports.append(report)
        
    for i in range(0, len(tempSafeReports)):
        report = tempSafeReports[i]
        if isSafe(report): safeReports += 1
    return safeReports

initializeInput(file) 
print(checkSafeReports())
