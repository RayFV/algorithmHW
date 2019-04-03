#1. 輸入string
inputStr = input("請輸入中文字串：")
strDict = {}

#2. 生產各種組合
def genStr(preStr,postStr):
    postCharlist = list(postStr)
    print("1." , preStr)
    print("2." , postCharlist)
    if len(postCharlist)<=0 :
        strDict[preStr] = ""
        print(strDict)
    else :     
        for charIdx in range(len(postCharlist)) :
            nowChar = postCharlist[charIdx]
            print("3." , nowChar)
            newList = postCharlist.copy()
            del newList[charIdx]
            print("4." , newList)
            genStr(preStr+nowChar,newList)
genStr("",inputStr)

#3. 印出來
count = 0
for string in strDict :
    count += 1
    print(str(count) + ". " + string)
print( "共"+str(count)+"種文字組合" )