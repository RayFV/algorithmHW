str = input("請輸入中文字串：")
#str = "花世界"

# mostLength=1
# for i in range(1, len(str) + 1):
#     mostLength *= i

def test(list):
    result = []
    if len(list) == 2:
        result.append(list)
        temp = [list[1], list[0]]
        listAppendWithoutDuplicate(result, temp)
    elif len(list) >= 3:
        for i in range(len(list)):
            for j in test(list[1:]):
                temp = list[:1] + j
                listAppendWithoutDuplicate(result, temp)
            if(i != len(list) - 1):
                list[0], list[i+1] = list[i+1], list[0]
            #print(result)
    return result

def listAppendWithoutDuplicate(originalList, newItem):
    if newItem not in originalList:
        originalList.append(newItem)


def displayResult(result):
    for i, item in enumerate(result):
        print("{0}. {1}".format(i+1, ''.join(item)))
    
    print("共{0}種文字組合".format(len(result)))

strList = list(str)
displayResult(test(strList))