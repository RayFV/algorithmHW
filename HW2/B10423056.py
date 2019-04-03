import re

# userInput = input("input:")
userInput = '4*(8+2)'

separators = re.compile(r'([+\-*/()])')
operator = {'(': 0, '+': 5, '-': 5, '*': 10, '/': 10}

postfixStack = []


class Tree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def isNumber(self):
        return self.data.isdigit()

    def isOperator(self):
        return self.data in operator

    def displayInfix(self):
        if self.left is not None:
            print('(', end='')
            self.left.displayInfix()
        print(self.data, end='')
        if self.right is not None:
            self.right.displayInfix()
            print(')', end='')
        

    def displayPostfix(self):
        if self.left is not None:
            self.left.displayPostfix()
        if self.right is not None:
            self.right.displayPostfix()
        print(self.data, end='')

    def displayPrefix(self):
        print(self.data, end='')
        if self.left is not None:
            self.left.displayPrefix()
        if self.right is not None:
            self.right.displayPrefix()


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


def createTreeWithPosfix(current, postfix):
    current.data = postfix.pop()

    if not postfix or not current.isOperator():
        return

    current.right = Tree()
    createTreeWithPosfix(current.right, postfix)

    current.left = Tree()
    createTreeWithPosfix(current.left, postfix)





infix = list(filter(None, separators.split(userInput)))
infixToPostfix(infix)
print("InfixList:", infix)
print("PostfixStack:", postfixStack)


root = Tree()
createTreeWithPosfix(root, postfixStack)
print("\nInfix: ")
root.displayInfix()
print("\n\nPostfix: ")
root.displayPostfix()
print("\n\nPrefix: ")
root.displayPrefix()
print()
print()