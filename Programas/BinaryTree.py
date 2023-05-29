#Implementación recursiva
class BinaryTree:
    def __init__(self, value = None, storedValue = None):
        self.root = value
        self.storedValue = storedValue
        self.left_tree = None
        self.right_tree = None
        self.balance_factor = 0

    def getRoot(self):
        return self.root

    def getRight(self):
        return self.right_tree

    def getLeft(self):
        return self.left_tree

    def getStoredValue(self):
        return self.storedValue

    def setRoot(self, new_root):
        self.root = new_root

    def setRight(self, new_tree):
        if isinstance(new_tree, BinaryTree):
            self.right_tree = new_tree

    def setLeft(self, new_tree):
        if isinstance(new_tree, BinaryTree):
            self.left_tree = new_tree

    def __str__(self):
        return 'Leaf(' + str(self.root) + ',' + str(self.storedValue) +','+ str(self.balance_factor)+ ')'

    def inOrder(self):
        if self.left_tree is not None:
            self.left_tree.inOrder()
        print(self.root)
        if self.right_tree is not None:
            self.right_tree.inOrder()

    def preOrder(self):
        print(self.root)
        if self.left_tree is not None:
            self.left_tree.preOrder()
        if self.right_tree is not None:
            self.right_tree.preOrder()

    def posOrder(self):
        if self.left_tree is not None:
            self.left_tree.posOrder()
        if self.right_tree is not None:
            self.right_tree.posOrder()
        print(self.root)

    def inOrderValue(self, list):
        if self.left_tree is not None:
            self.left_tree.inOrderValue(list)
        list.append(self)
        if self.right_tree is not None:
            self.right_tree.inOrderValue(list)

    def preOrderValue(self, list):
        list.append(self)
        if self.left_tree is not None:
            self.left_tree.preOrderValue(list)
        if self.right_tree is not None:
            self.right_tree.preOrderValue(list)

    def posOrderValue(self, list):
        if self.left_tree is not None:
            self.left_tree.posOrderValue(list)
        if self.right_tree is not None:
            self.right_tree.posOrderValue(list)
        list.append(self)

    def get(self, root):
        return self.search(root)

    def search(self, root):
        if self.root == root:
            return self.storedValue
        if root < self.root:
            return self.left_tree.get(root) if self.left_tree is not None else None
        return self.right_tree.get(root) if self.right_tree is not None else None

    def minimum(self):
        if self.left_tree is not None:
            return self.left_tree.minimum()
        return self

    def maximum(self):
        if self.right_tree is not None:
            return self.right_tree.maximum()
        return self

    def isEmpty(self):
        return self.root is None

    def insert(self, key, value):
        if not self.isEmpty():
            if key >= self.root:
                    if self.right_tree is not None:
                        self.right_tree.insert(key,value)
                    else:
                        self.setRight(BinaryTree(key, value))
            else:
                if self.left_tree is not None:
                    self.left_tree.insert(key, value)
                else:
                    self.setLeft(BinaryTree(key, value))
        else:
            self.root, self.storedValue = key, value
        self.calculateBalanceFactor()
        #Estoy desbalanceado ? , Si si, balanceeme

    def insertMany(self, data = []):
        for ele in data:
            self.insert(ele[0], ele[1])

    def is_leaf(self):
        return self.left_tree is None and self.right_tree is None
    # Esta altura no tiene en cuenta la raiz
    def getHeight(self):
        if self.is_leaf():
            return 0
        left_height, right_height = 0,0
        if self.right_tree is not None:
            right_height = 1 + self.right_tree.getHeight()

        if self.left_tree is not None:
            left_height = 1 + self.left_tree.getHeight()


        return max(right_height, left_height)

    def calculateBalanceFactor(self):
        left_height, right_height = 0, 0
        if self.right_tree is not None:
            right_height = 1 + self.right_tree.getHeight()
        if self.left_tree is not None:
            left_height = 1 + self.left_tree.getHeight()
        self.balance_factor = right_height - left_height

def main():

    bn_root = BinaryTree()

    bn_root.insertMany([
        (7,7),
        (13,13),
        (9,9)
    ])

    print('========================= InOrden =========================')
    bn_root.inOrder()
    inOrderValue = []
    bn_root.inOrderValue(inOrderValue)
    print(list(map(str,inOrderValue)))
    print('========================= PreOrden =========================')
    bn_root.preOrder()
    preOrderValue = []
    bn_root.preOrderValue(preOrderValue)
    print(list(map(str, preOrderValue)))
    print('========================= PosOrden =========================')
    bn_root.posOrder()
    posOrderValue = []
    bn_root.posOrderValue(posOrderValue)
    print(list(map(str, posOrderValue)))
    print('========================= Search =========================')
    print(bn_root.get(5))
    print('========================= Minimum =========================')
    print(bn_root.minimum())
    print('========================= Maximum =========================')
    print(bn_root.maximum())
    print('========================= Height =========================')
    print(bn_root.getHeight())

    array = []
    inOrderVal = bn_root.inOrderValue(array)
    print('Checking BALANCE fACTOR')
    bn_root.calculateBalanceFactor()
    print(list(map(str, array)))

    new_tree = BinaryTree()
    new_tree.insertMany([(i,i) for i in range(10)])

main()

#Hashable