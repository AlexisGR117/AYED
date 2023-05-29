class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.root = value
        self.left = left
        self.right = right

    def get_root(self):
        return self.root

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_root(self, new_root):
        self.root = new_root

    def set_left(self, new_tree):
        if isinstance(new_tree, BinaryTree) or new_tree is None:
            self.left = new_tree

    def set_right(self, new_tree):
        if isinstance(new_tree, BinaryTree) or new_tree is None:
            self.right = new_tree

    def __str__(self):
        return "Leaf(" + str(self.root) + ')'


def solve(arbol, respuesta):
    if arbol.left is not None and arbol.right is not None:
        if arbol.left.get_root() > arbol.get_root() or arbol.right.get_root() > arbol.get_root():
            return False
        else:
            respuesta = solve(arbol.get_left(), respuesta)
            respuesta = solve(arbol.get_right(), respuesta)
    elif arbol.right is not None:
        if arbol.right.get_root() > arbol.get_root():
            return False
        else:
            respuesta = solve(arbol.get_right(), respuesta)
    elif arbol.left is not None:
        if arbol.left.get_root() > arbol.get_root():
            return False
        else:
            respuesta = solve(arbol.get_left(), respuesta)
    return respuesta


def main():
    bn_root = BinaryTree(15)
    bn_l1 = BinaryTree(12)
    bn_l2 = BinaryTree(10)
    bn_l3 = BinaryTree(8)
    bn_l4 = BinaryTree(9)
    bn_l5 = BinaryTree(5)
    bn_l6 = BinaryTree(3)
    bn_l7 = BinaryTree(1)

    bn_root.set_left(bn_l1)
    bn_root.set_right(bn_l2)
    bn_l1.set_left(bn_l3)
    bn_l1.set_right(bn_l4)
    bn_l2.set_left(bn_l5)
    bn_l2.set_right(bn_l6)
    bn_l4.set_left(bn_l7)

    print("El arbol es un max-heap, así que la función debería retornar True:")
    print(solve(bn_root, True))
    print("Ahora voy a cambiar el valor de un subarbol para que sea mayor que el de la raiz.")
    bn_l4.set_root(20)
    print("La función debería retornar False:")
    print(solve(bn_root, True))

main()
