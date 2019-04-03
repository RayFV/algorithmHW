import re

# userInput = input("input:")
userInput = '((8+2)*4)'

separators = re.compile(r'([+\-*/()])')
operator = { '(':0, '+': 5, '-': 5,'*': 10, '/': 10}

postfixStack = []


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def isNumber(self):
        return self.data.isdigit()

    def isOperator(self):
        return self.data in operator


def infixToPostfix(infix):
    tempStack = []
    for item in infix:
        if item == '(':
            tempStack.append(item)
        elif item == ')':
            tempItem = tempStack.pop()
            while(tempItem != '('):
                postfixStack.append(tempItem)
                tempItem = tempStack.pop()
        elif item in operator:
            while(tempStack and operator[item] <= operator[tempStack[-1]]):
                postfixStack.append(tempStack.pop())
            tempStack.append(item)
        else:
            postfixStack.append(item)

    while(tempStack):
        postfixStack.append(tempStack.pop())


# root = Tree()
infix = list(filter(None, separators.split(userInput)))
print(infix)
infixToPostfix(infix)
print("Postfix:",postfixStack)
