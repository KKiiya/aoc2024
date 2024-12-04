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

def isSafeValues(report):
    for i in range(0, len(report)):
        reportCopy = list(report.copy())
        reportCopy.pop(i)
        if isSafe(reportCopy): 
            print(str(report) + " is safe if removed " + str(report[i]))
            print("Final safe report: " + str(reportCopy))
            return True

        #print("Report is safe if " + str(report[i]) + " is removed")
        #print(report)
        return False
            
    return False


def checkSafeReports():
    safeReports = 0
    tempSafeReports = []
    for i in range(0, len(reports)):
        # print("Scanning repot Nº" + str(i))
        report = list(reports[i])
        difference = report[0] - report[1]

        decreasing = False
        if difference > 0: decreasing = True

        safe = True
        for j in range(1, len(report)):
            if decreasing and report[j-1] <= report[j]: 
                safe = isSafeValues(report)
                #print("Decreasing " + str(report) + " report has a greater value which is: " + str(report[j]))
                break
            elif (not decreasing) and report[j-1] >= report[j]: 
                safe = isSafeValues(report)
                #print("Increasing " + str(report) + " report has a smaller value which is: " + str(report[j]))
                break
        #if safe: tempSafeReports.append(report)
        
    for i in range(0, len(tempSafeReports)):
        report = tempSafeReports[i]
        if isSafe(report): 
            #print(report)
            safeReports += 1
    return safeReports

initializeInput(file) 
print(checkSafeReports())
