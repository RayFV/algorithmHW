import re

separators = re.compile(r'([+\-*/()])')
operator = {'(': 0, '+': 5, '-': 5, '*': 10, '/': 10}


class Tree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def isNumber(self):
        return self.data.isdigit()

    def isOperator(self):
        return self.data in operator


def isOperator(data):
    return data in operator


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


def displayTree(tree):
    if tree.left is not None:
        displayTree(tree.left)
    print(tree.data)
    if tree.right is not None:
        displayTree(tree.right)


# userInput = input("input:")
userInput = '(8+2)*4'


postfixStack = []


infix = list(filter(None, separators.split(userInput)))
print("Infix:", infix)
infixToPostfix(infix)
print("Postfix:", postfixStack)


root = Tree()
createTreeWithPosfix(root, postfixStack)
displayTree(root)
