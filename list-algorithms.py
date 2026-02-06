# property algorithm
def greaterThanZero(inputList):
    allPositive = True
    for i in range(len(inputList)):
        if inputList[i] < 0:
            allPositive = False
    return allPositive

# max value algorithm
def maxValue(inputList):
    maxItem = inputList[0]
    for i in range(1, len(inputList)):
        if inputList[i] > maxItem:
            maxItem = inputList[i]
    return maxItem

# update items algorithm
def multiplyBy100(inputList):
    tempList = []
    for value in inputList:
        tempList.append(value*100)
    return tempList

# rotate algorithm
def rotateBy1(inputList):
    first = inputList[0]
    for i in range(1, len(inputList)):
        inputList[i-1] = inputList[i]
    inputList[len(inputList)-1] = first
    return inputList

myNumberList = [10, 3, 5, 11, 15, 11, 13, 3, 7, 11, 1, 5, 7, 14, 4, 9, 10, 11, 11, 8, 12, 1, 12, 1, 2]
# testing functions below
print(greaterThanZero(myNumberList))
print(maxValue(myNumberList))
print(multiplyBy100(myNumberList))
print(rotateBy1(myNumberList))