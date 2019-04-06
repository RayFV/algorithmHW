'''
無法處理8(2+3)之類的式子
只能輸入中序式子

做法：
先把輸入的中序轉成後序，再建成二元樹。
然後可以列印出中序、後序、前序，並且可以運算出答案

輸出樹狀結構圖的部分需要用到Graphviz2.38
'''

import re
import os

OPERATOR = {'(': 0, '+': 5, '-': 5, '*': 10, '/': 10}


class Node:
    id_count = 0

    def __init__(self, data=None):
        self.id = str(Node.id_count)
        Node.id_count += 1
        self.data = data
        self.left = None
        self.right = None

    def isOperator(self):
        return self.data in OPERATOR

    def getInfix(self):
        result = []
        if self.left:
            result.append('(')
            result = result + self.left.getInfix()
        result.append(self)
        if self.right:
            result = result + self.right.getInfix()
            result.append(')')
        return result

    def getInfixText(self):
        infix = self.getInfix()
        result = " ".join(
            [node.data if node not in ['(', ')'] else node for node in infix])
        return result

    def getPostfix(self):
        result = []
        if self.left:
            result = result + self.left.getPostfix()
        if self.right:
            result = result + self.right.getPostfix()
        result.append(self)
        return result

    def getPostfixText(self):
        postfix = self.getPostfix()
        result = " ".join([node.data for node in postfix])
        return result

    def getPrefix(self):
        result = []
        result.append(self)
        if self.left:
            result = result + self.left.getPrefix()
        if self.right:
            result = result + self.right.getPrefix()
        return result

    def getPrefixText(self):
        prefix = self.getPrefix()
        result = " ".join([node.data for node in prefix])
        return result

    def getResult(self):
        if not self.isOperator:
            return
        prefix = self.getPrefixText().strip().split(' ')
        tempStack = []
        while(prefix):
            if(prefix[-1] in OPERATOR):
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

    # BFS練習
    def getBFS(self):
        bfsResult = []
        queue = []
        queue.append(self)
        id_count = 0
        while(queue):
            current = queue.pop(0)
            bfsResult.append(current)
            id_count += 1
            if(current.isOperator()):
                queue.append(current.left)
                queue.append(current.right)
        return bfsResult


def infixToPostfix(infix):
    postfixStack = []
    tempStack = []
    for item in infix:
        if item == '(':
            tempStack.append(item)
        elif item == ')':
            tempItem = tempStack.pop()
            while(tempItem != '('):
                postfixStack.append(tempItem)
                tempItem = tempStack.pop()
        elif item in OPERATOR:
            while(tempStack and OPERATOR[item] <= OPERATOR[tempStack[-1]]):
                postfixStack.append(tempStack.pop())
            tempStack.append(item)
        else:
            postfixStack.append(item)

    while(tempStack):
        postfixStack.append(tempStack.pop())

    return postfixStack


def createTreeWithPosfix(currentNode, postfixStack):
    currentNode.data = postfixStack.pop()

    if not postfixStack or not currentNode.isOperator():
        return

    currentNode.right = Node()
    createTreeWithPosfix(currentNode.right, postfixStack)

    currentNode.left = Node()
    createTreeWithPosfix(currentNode.left, postfixStack)


# Create tree structure graph with graphviz
def generateTreeGraph(root):
    treeStringResult = 'graph {\n  size="7,5";\n  node [color=goldenrod2, style=filled];\n  '

    bfs = root.getBFS()  # 不一定需要使用BFS

    for node in bfs:
        # create label with unique id
        treeStringResult += node.id + ' [label="' + node.data + '"];\n  '

        # create Vertices and Edge
        if node.left:
            treeStringResult += node.id + ' -- ' + node.left.id + ';\n  '
        if node.right:
            treeStringResult += node.id + ' -- ' + node.right.id + ';\n  '

    treeStringResult = treeStringResult.rstrip() + "\n}"  # Close

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
    print("DONE. \n\n")

    # print(treeStringResult)


userInput = input("請輸入中序算術式: ").replace(" ", "")
# userInput = '(((8+11)-(6*4))/((20-15)*6))'

separators = re.compile(r'([+\-*/()])')

# 用separators切割并保留，這是考慮到有小數點的可能而使用的切割法
infix = list(filter(None, separators.split(userInput)))
print(infix)

postfixStack = infixToPostfix(infix)

root = Node()  # Crete root
createTreeWithPosfix(root, postfixStack)

print("\nInfix: ", root.getInfixText(), end="\n\n")

print("Postfix: ", root.getPostfixText(), end="\n\n")

print("Prefix: ", root.getPrefixText(), end="\n\n")

print("Result: ", root.getResult(), end="\n\n")

generateTreeGraph(root)
