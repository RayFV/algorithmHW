

FILENAME = "Test.dat"

limit = 500 #數量

def getNumberDataList():
    allData = []
    dataFile = open(FILENAME,"r")
    for line in dataFile:
        if(len(allData) > limit):
            break
        splitedList = line.split(" ")
        del splitedList[-1] #remove '\n'
        splitedList = list(map(int, splitedList)) # convert to int
        allData += splitedList
    dataFile.close()
    return allData
