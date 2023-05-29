import random


class Node:
    def __init__(self, value):
        # Definicion estructural
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    # Definicion Comportamental
    def getValue(self):
        return self.value

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setValue(self, value):
        self.value = value

    def getHeight(self):
        return self.height

    def setRight(self, right):
        self.right = right

    def setLeft(self, left):
        self.left = left

    def setHeight(self, height):
        self.height = height

    def getBalance(self):
        left, right = self.getLeft(), self.getRight()
        leftH, rightH = left.getHeight() if left else 0, right.getHeight() if right else 0
        return ( leftH - rightH )

    def printNode(self, node):
        return (str(node.getValue())) if node is not None else ('EMPTY')


class Tree:
    def __init__(self, root, balanced = False):
        self.root = root
        # if Balanced AVL - otherwise BST
        self.balanced = balanced

    def getRoot(self):
        return self.root

    def setRoot(self, root):
        self.root = root

    #Walk methods
    def inorderWalk(self, node):
        if node is not None:
            self.inorderWalk(node.getLeft())
            print(node.getValue())
            self.inorderWalk(node.getRight())

    def preorderWalk(self, node):
        if node is not None:
            print(node.getValue())
            self.preorderWalk(node.getLeft())
            self.preorderWalk(node.getRight())

    def posOrderWalk(self, node):
        if node is not None:
            self.posOrderWalk(node.getLeft())
            self.posOrderWalk(node.getRight())
            print(node.getValue())

    def searchNode(self, node, searchKey, cnt=0):
        if node is None or searchKey == node.getValue():
            return (node, cnt)

        return self.searchNode(node.getLeft() if searchKey < node.getValue() else node.getRight(), searchKey, cnt + 1)

    def minimum(self):
        node = self.getRoot()
        while node.getLeft() is not None:
            node = node.getLeft()
        return node

    def maximum(self):
        node = self.getRoot()
        while node.getRight() is not None:
            node = node.getRight()
        return node

    #Generic Insertion method
    def insert(self, node):
        if not self.balanced :
            self.insertBST(node)
        else:
            self.insertAVL(node)

    # BST Insertion functions
    def searchEmptySpot(self, key):
        node = self.getRoot()
        spot = None
        while node is not None:
            spot = node
            node = node.getLeft() if key < node.getValue() else node.getRight()
        return spot



    def insertBST(self, node):
        spot = self.searchEmptySpot(node.getValue())

        if spot is None:
            self.setRoot(node)
        elif node.getValue() < spot.getValue():
            spot.setLeft(node)
        else:
            spot.setRight(node)


    #AVL Insertion functions
    def getHeight(self, node):
        if node is None:
            return 0
        return node.getHeight()

    def setHeight(self, node):
        if node is not None :
            left, right = node.getLeft(), node.getRight()
            node.setHeight(max(self.getHeight(left),  self.getHeight(right)) + 1)

    def insertAVL(self, nodeIns):
        self.setRoot(self._insertAVL(self.getRoot(), nodeIns))

    def _insertAVL(self, node, nodeIns):
        if node is None:
            return nodeIns
        if node.getValue() > nodeIns.getValue():
            node.setLeft( self._insertAVL(node.getLeft(), nodeIns) )
        else:
            node.setRight(self._insertAVL(node.getRight(), nodeIns))
        #Update node Height
        self.setHeight(node)
        diffBal = node.getBalance()

        value = nodeIns.getValue()

        #Determinate left Rotate
        if diffBal > 1 and value < node.getLeft().getValue():
            return self.rotateRight(node)

        #Determinate right Rotate
        if diffBal < -1 and value > node.getRight().getValue():
            return self.rotateLeft(node)

        #Determinate left-right Rotate
        if diffBal > 1 and value > node.getLeft().getValue():
            node.setLeft(self.rotateLeft(node.getLeft()))
            return self.rotateRight(node)

        #Determinate right-left Rotate
        if diffBal < -1 and value < node.getRight().getValue():
            node.setRight(self.rotateRight(node.getRight()))
            return self.rotateLeft(node)

        return node

    def rotateRight(self, node):
        left = node.getLeft()
        leftR = left.getRight()
        #Rotate
        left.setRight(node)
        node.setLeft(leftR)
        #Update Heights
        self.setHeight(left)
        self.setHeight(node)
        return left

    def rotateLeft(self, node):
        right = node.getRight()
        rightL = right.getLeft()
        # Rotate
        right.setLeft(node)
        node.setRight(rightL)
        # Update Heights
        self.setHeight(right)
        self.setHeight(node)
        return right

    def insertList(self, lst):
        for e in lst:
            self.insert(Node(e))



MAX = 1E4
MAX_SIZE = 8
lst = [(random.randrange(0, MAX)) for i in range(MAX_SIZE)]

def searchInTree(tree, key):
    handler = Node(None)
    searchResult = tree.searchNode(tree.getRoot(), key)
    print('Query: ', handler.printNode(searchResult[0]),'Steps taken: ',searchResult[1])

def testTree(tree):
    print(lst)
    tree.insertList(lst)
    print('============INORDEN============')
    tree.inorderWalk(tree.getRoot())
    print('============PREORDEN============')
    tree.preorderWalk(tree.getRoot())
    print('============POSORDEN============')
    tree.posOrderWalk(tree.getRoot())
    print('============MAX============')
    mx = tree.maximum()
    print(mx.getValue() if mx is not None else None)
    print('============MIN============')
    mn = tree.minimum()
    print(mn.getValue() if mn is not None else None)
    searchCandidate = lst[random.randrange(0, MAX_SIZE)]
    print('============SEARCHING RANDOM CANDIDATE============')
    searchInTree(tree, searchCandidate)
    print('============SEARCHING ALL MEMBERS============')
    for e in lst:
        searchInTree(tree, e)


def main():
    bst = Tree(None)
    #Test Case BST
    print('===================TESTING BST TREE ==============================')
    testTree(bst)
    #Test Case AVL
    print('===================TESTING AVL TREE ==============================')
    avl = Tree(None, True)
    testTree(avl)
    # Test Case AVL


main()