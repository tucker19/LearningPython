
def collatzCycle(testNum):
    collatzList = [testNum]
    while(testNum != 1):
        if(testNum % 2 == 0):
            testNum = testNum/2
        else:
            testNum = 3*testNum+1
            
        collatzList.append(testNum)
        
    return collatzList

def printCollatzCycle(collatzList):
    collatzStrList = []
    for collatz in collatzList:
        collatzStr = str(collatz)
        if(collatzStr.__contains__(".0")):
            collatzStr = collatzStr[0:len(collatzStr) - 2]
            
        collatzStrList.append(collatzStr)
    
    return collatzStrList

testNum = int(input("What number would you like to test? "))
collatzList = collatzCycle(testNum)
    
print("Starting number: %d" % collatzList[0])
print("Length of Collatz Cycle: %d" % len(collatzList))
print("Collatz Cycle: %s" % " -> ".join(printCollatzCycle(collatzList)))