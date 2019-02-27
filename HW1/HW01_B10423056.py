#str = input("請輸入中文字串：")
str = "0012"

strLen = len(str)

mostLength=1
for i in range(1, strLen + 1):
    mostLength *= i

allList = [[0] * strLen for _ in range(mostLength)]

def test(list):
    result = []
    if len(list) == 2:
        result.append(list)
        swap = [list[1], list[0]]
        result.append(swap)
    elif len(list) >= 3:
        for i in range(len(list)):
            for j in test(list[1:]):
                temp = list[:1] + j
                if temp not in result:
                    result.append(temp)
            if(i != len(list) - 1):
                list[0], list[i+1] = list[i+1], list[0]
            
            print(result)
    return result

strList = list(str)
result = test(strList)

print("length", len(result))
print(result)