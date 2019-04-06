'''
無法處理8(2+3)之類的式子
只能輸入中序式子

做法：
先把輸入的中序轉成後序，再建成二元樹。
然後可以列印出中序、後序、前序，並且可以運算出答案
'''

import re
import os

# userInput = input("input:")
userInput = '(((8+11)-(6*4))/((20-15)*6))'

separators = re.compile(r'([+\-*/()])')
operator = {'(': 0, '+': 5, '-': 5, '*': 10, '/': 10}

postfixStack = []

# 用separators切割并保留，這是考慮到有小數點的可能而使用的切割法
infix = list(filter(None, separators.split(userInput)))


class Tree:
    def __init__(self, data=None):
        self.bfsId = None
        self.data = data
        self.left = None
        self.right = None
        self.countLeftChildren = 0
        self.countRightChildren = 0
        self.depth = 1

    def isNumber(self):
        return self.data.isdigit()

    def isOperator(self):
        return self.data in operator

    def getInfix(self):
        result = ""
        if self.left is not None:
            result = result + '(' + self.left.getInfix()
        result = result + ' ' + self.data + ' '
        if self.right is not None:
            result = result + self.right.getInfix() + ')'
        return result

    def getPostFix(self):
        result = ""
        if self.left is not None:
            result += self.left.getPostFix()
        if self.right is not None:
            result += self.right.getPostFix()
        result = result + self.data + ' '
        return result

    def getPrefix(self):
        result = ""
        result = result + self.data + ' '
        if self.left is not None:
            result += self.left.getPrefix()
        if self.right is not None:
            result += self.right.getPrefix()
        return result

    def getResult(self):
        if not self.isOperator:
            return

        prefix = self.getPrefix().strip().split(' ')
        tempStack = []

        while(prefix):
            if(prefix[-1] in operator):
                op = prefix.pop()
                a = float(tempStack.pop())
                b = float(tempStack.pop())
                if(op == '+'):
                    tempStack.append(a + b)
                elif(op == '-'):
                    tempStack.append(a - b)
                elif(op == '*'):
                    tempStack.append(a * b)
                elif(op == '/'):
                    tempStack.append(a / b)
            else:
                tempStack.append(prefix.pop())

        return tempStack.pop()

    def getTotalChild(self):
        return self.countLeftChildren + self.countRightChildren

    def getBFS(self):
        bfsResult = []
        queue = []
        queue.append(self)
        id_count = 0
        while(queue):
            current = queue.pop(0)
            bfsResult.append(current)
            current.bfsId = str(id_count)
            id_count += 1
            if(current.isOperator()):
                queue.append(current.left)
                queue.append(current.right)
        return bfsResult


def infixToPostfix():
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


def createTreeWithPosfix(current):
    current.data = postfixStack.pop()

    if not postfixStack or not current.isOperator():
        return

    current.right = Tree()
    current.right.depth += current.depth
    current.countRightChildren += 1
    createTreeWithPosfix(current.right)
    current.countRightChildren += current.right.getTotalChild()

    current.left = Tree()
    current.left.depth += current.depth
    current.countLeftChildren += 1
    createTreeWithPosfix(current.left)
    current.countLeftChildren += current.left.getTotalChild()


# Create tree structure graph with graphviz
def generateTreeGraph(root):
    treeStringResult = 'graph {\n  size="7,5";\n  node [color=goldenrod2, style=filled];\n  '
    bfs = root.getBFS()

    for node in bfs:
        # create label with unique id
        treeStringResult += node.bfsId + ' [label="' + node.data + '"];\n  '

        # create Vertices and Edge
        if node.left is not None:
            treeStringResult += node.bfsId + ' -- ' + node.left.bfsId + ';\n  '
        if node.right is not None:
            treeStringResult += node.bfsId + ' -- ' + node.right.bfsId + ';\n  '

    treeStringResult += "\n}"  # Close

    # Write to file
    fileName = 'treeGraph.dot'
    myfile = open(fileName, 'w')
    myfile.write(treeStringResult)
    myfile.close()

    # Run command
    print("Generating tree Graph...")
    os.system(".\\Graphviz2.38\\bin\\dot.exe -Tpng treeGraph.dot -o treeGraph.png")
    print("Successfully write the " + fileName + " file")

    print("Opening image...")
    os.system("treeGraph.png")

    # print(treeStringResult)


infixToPostfix()
# print("InfixList:", infix)
# print("PostfixStack:", postfixStack)

root = Tree()
createTreeWithPosfix(root)

print("\nInfix: ", root.getInfix(), end="\n\n")

print("Postfix: ", root.getPostFix(), end="\n\n")

print("Prefix: ", root.getPrefix(), end="\n\n")

print("Result: ", root.getResult(), end="\n\n")

generateTreeGraph(root)
