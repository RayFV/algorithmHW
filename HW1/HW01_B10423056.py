userInput = input("請輸入中文字串：")
#userInput = "花世界"

# mostLength=1
# for i in range(1, len(userInput) + 1):
#     mostLength *= i

def permutations(list):
    result = []
    if len(list) <= 1:
        return list
    if len(list) == 2:
        result.append(list)
        temp = [list[1], list[0]]
        listAppendWithoutDuplicate(result, temp)
    elif len(list) >= 3:
        for i in range(len(list)):
            list[0], list[i] = list[i], list[0]
            for j in permutations(list[1:]):
                temp = list[:1] + j
                listAppendWithoutDuplicate(result, temp)
            #print(result)
    return result

def listAppendWithoutDuplicate(originalList, newItem):
    if newItem not in originalList:
        originalList.append(newItem)

def displayResult(result):
    for i, item in enumerate(result):
        print("{0}. {1}".format(i+1, ''.join(item)))
    
    print("共{0}種文字組合".format(len(result)))

strList = list(userInput)
displayResult(permutations(strList))
