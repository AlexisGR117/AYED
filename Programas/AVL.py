class BinaryTree:
    def __init__(self, value = None, stored_value = None):
        self.root = value
        self.stored_value = stored_value
        self.left_tree = None
        self.right_tree = None
        self.higher = None
        self.balance_factor = 0

    def get_root(self):
        return self.root

    def get_stored_value(self):
        return self.stored_value

    def get_left(self):
        return self.left_tree

    def get_right(self):
        return self.right_tree

    def get_higher(self):
        return self.higher

    def get_balance_factor(self):
        return self.balance_factor

    def set_root(self, new_root):
        self.root = new_root

    def set_stored_value(self, new_stored_value):
        self.root = new_stored_value

    def set_left(self, new_tree):
        if isinstance(new_tree, BinaryTree) or new_tree is None:
            self.left_tree = new_tree

    def set_right(self, new_tree):
        if isinstance(new_tree, BinaryTree) or new_tree is None:
            self.right_tree = new_tree

    def set_higher(self, new_tree):
        if isinstance(new_tree, BinaryTree) or new_tree is None:
            self.higher = new_tree

    def __str__(self):
        if self.left_tree is not None and self.right_tree is not None and self.get_higher() is not None:
            return "Nodo(" + str(self.left_tree.root) + ", " + str(self.root) + ", " + str(self.right_tree.root) + ", " + str(self.get_higher().root) + ", " + str(self.balance_factor) + ')'
        elif self.left_tree is not None and self.right_tree is not None:
            return "Nodo(" + str(self.left_tree.root) + ", " + str(self.root) + ", " + str(self.right_tree.root) + ", None, " + str(self.balance_factor) + ')'
        elif self.left_tree is not None and self.get_higher() is not None:
            return "Nodo(" + str(self.left_tree.root) + ", " + str(self.root) + ", None, " + str(self.get_higher().root) + ", " + str(self.balance_factor) + ')'
        elif self.right_tree is not None and self.get_higher() is not None:
            return "Nodo(" + "None, " + str(self.root) + ", " + str(self.right_tree.root) + ", " + str(self.get_higher().root) + ", " + str(self.balance_factor) + ')'
        elif self.right_tree is not None:
            return "Nodo(" + "None, " + str(self.root) + ", " + str(self.right_tree.root) + ", None, " + str(self.balance_factor) + ')'
        elif self.left_tree is not None:
            return "Nodo(" + str(self.left_tree.root) + ", " + str(self.root) + ", None, " + ", None, " + str(self.balance_factor) + ')'
        else:
            return "Nodo(" + "None, " + str(self.root) + ", None, " + str(self.get_higher().root) + ", " + str(self.balance_factor) + ')'

    def in_order(self):
        if self.left_tree is not None:
            self.left_tree.in_order()
        print(self.root)
        if self.right_tree is not None:
            self.right_tree.in_order()

    def pre_order(self):
        print(self.root)
        if self.left_tree is not None:
            self.left_tree.pre_order()
        if self.right_tree is not None:
            self.right_tree.pre_order()

    def post_order(self):
        if self.left_tree is not None:
            self.left_tree.post_order()
        if self.right_tree is not None:
            self.right_tree.post_order()
        print(self.root)

    def in_order_value(self, list):
        if self.left_tree is not None:
            self.left_tree.in_order_value(list)
        list.append(self)
        if self.right_tree is not None:
            self.right_tree.in_order_value(list)

    def pre_order_value(self, list):
        list.append(self)
        if self.left_tree is not None:
            self.left_tree.pre_order_value(list)
        if self.right_tree is not None:
            self.right_tree.pre_order_value(list)

    def post_order_value(self, list):
        if self.left_tree is not None:
            self.left_tree.post_order_value(list)
        if self.right_tree is not None:
            self.right_tree.post_order_value(list)
        list.append(self)

    def search(self, root):
        if self.root == root:
            return self
        elif self.root > root:
            return self.left_tree.search(root) if self.left_tree is not None else None
        return self.right_tree.search(root) if self.right_tree is not None else None

    def minimum(self):
        if self.left_tree is not None:
            return self.left_tree.minimum()
        return self

    def maximum(self):
        if self.right_tree is not None:
            return self.right_tree.maximum()
        return self

    def is_empty(self):
        return self.root is None

    def insert(self, key, value):
        if not self.is_empty():
            if key >= self.root:
                if self.right_tree is not None:
                    self.right_tree.insert(key, value)
                else:
                    new = BinaryTree(key, value)
                    new.set_higher(self)
                    self.set_right(new)
            else:
                if self.left_tree is not None:
                    self.left_tree.insert(key, value)
                else:
                    new = BinaryTree(key, value)
                    new.set_higher(self)
                    self.set_left(new)
        else:
            self.root, self.stored_value = key, value
        self.calculate_balance_factor()
        element = self.search(key)
        self.rotar(element)


    def insert_many(self, data=[]):
        for dat in data:
            self.insert(dat[0], dat[1])

    def is_leaf(self):
        return self.left_tree is None and self.right_tree is None

    def get_height(self):
        if self.is_leaf():
            return 0
        left_height, right_height = 0, 0
        if self.right_tree is not None:
            right_height = 1 + self.right_tree.get_height()
        if self.left_tree is not None:
            left_height = 1 + self.left_tree.get_height()
        return max(right_height, left_height)

    def calculate_balance_factor(self):
        left_height, right_height = 0, 0
        if self.right_tree is not None:
            right_height = 1 + self.right_tree.get_height()
        if self.left_tree is not None:
            left_height = 1 + self.left_tree.get_height()
        self.balance_factor = right_height - left_height

    def predecesor(self):
        if self.get_left() is not None:
            return self.get_left().maximum()
        else:
            higher = self.higher
            element = self
            while higher is not None and element == higher.get_left():
                element = higher
                higher = element.higher
            if higher is None:
                return None
            else:
                return higher

    def sucesor(self):
        if self.get_right() is not None:
             return self.get_right().minimum()
        else:
            higher = self.higher
            element = self
            while higher is not None and element == higher.get_right():
                element = higher
                higher = element.higher
            if higher is None:
                return None
            else:
                return higher

    def delete_raiz(self):
        if self.is_leaf():
            self.root, self.stored_value = None, None
        elif self.left_tree is None or self.right_tree is None:
            if self.left_tree is None:
                sucesor = self.right_tree
            else:
                sucesor = self.left_tree
            self.root, self.stored_value = sucesor.get_root(), sucesor.get_stored_value()
            self.right_tree, self.left_tree = sucesor.get_right(), sucesor.get_left()
            self.calculate_balance_factor()
        else:
            sucesor = self.sucesor()
            self.root, self.stored_value = sucesor.get_root(), sucesor.get_stored_value()
            self.get_left().set_higher(sucesor)
            if sucesor.higher != self:
                sucesor.higher.set_left(None)
                sucesor.higher.calculate_balance_factor()
            else:
                self.right_tree = sucesor.get_right()
            self.calculate_balance_factor()
            self.rotar(sucesor.higher)

    def delete(self, value):
        element = self.search(value)
        if element is not None:
            sucesor = None
            if element.higher is None:
                self.delete_raiz()
            else:
                if element.is_leaf():
                    if element.higher.get_left() == element:
                        element.higher.set_left(None)
                    else:
                        element.higher.set_right(None)
                    element.higher.calculate_balance_factor()
                elif element.get_left() is None:
                    if element.higher.get_left() == element:
                        element.higher.set_left(element.get_right())
                    else:
                        element.higher.set_right(element.get_right())
                    element.get_right().set_higher(element.higher)
                    element.higher.calculate_balance_factor()
                elif element.get_right() is None:
                    if element.higher.get_left() == element:
                        element.higher.set_left(element.get_left())
                    else:
                        element.higher.set_right(element.get_left())
                    element.get_left().set_higher(element.higher)
                    element.higher.calculate_balance_factor()
                else:
                    sucesor = element.sucesor()
                    sucesor.set_left(element.get_left())
                    sucesor.get_left().set_higher(sucesor)
                    if sucesor.higher != element:
                        sucesor.set_right(element.get_right())
                        sucesor.get_right().set_higher(sucesor)
                        sucesor.higher.set_left(None)
                        sucesor.higher.calculate_balance_factor()
                    sucesor.set_higher(element.higher)
                    if element.higher.get_left() == element:
                        element.higher.set_left(sucesor)
                    else:
                        element.higher.set_right(sucesor)
                    sucesor.calculate_balance_factor()
                    sucesor.higher.calculate_balance_factor()
            if sucesor is not None:
                self.rotar(sucesor.higher)
            else:
                self.rotar(element.higher)

    def recalculate_balance_factor(self, element):
        while element is not None:
            element.calculate_balance_factor()
            element = element.higher

    def rotation_left(self, element, hijo):
        hijo.set_higher(element.higher)
        if element.higher.get_left() == element:
            element.higher.set_left(hijo)
        else:
            element.higher.set_right(hijo)
        if hijo.get_left() is not None:
            element.set_right(hijo.get_left())
            hijo.get_left().set_higher(element)
        else:
            element.set_right(None)
        hijo.set_left(element)
        element.set_higher(hijo)
        self.recalculate_balance_factor(element)

    def rotation_right_left(self, element, hijo):
        hijo.get_left().set_higher(element)
        hijo.get_left().set_right(hijo)
        element.set_right(hijo.get_left())
        hijo.set_higher(hijo.get_left())
        hijo.set_left(None)
        hijo.calculate_balance_factor()
        self.rotation_left(element, element.get_right())

    def rotation_right(self, element, hijo):
        hijo.set_higher(element.higher)
        if element.higher.get_left() == element:
            element.higher.set_left(hijo)
        else:
            element.higher.set_right(hijo)
        if hijo.get_right() is not None:
            element.set_left(hijo.get_right())
            hijo.get_right().set_higher(element)
        else:
            element.set_left(None)
        hijo.set_right(element)
        element.set_higher(hijo)
        self.recalculate_balance_factor(element)

    def rotation_left_right(self, element, hijo):
        hijo.get_right().set_higher(element)
        hijo.get_right().set_left(hijo)
        element.set_left(hijo.get_right())
        hijo.set_higher(hijo.get_right())
        hijo.set_right(None)
        hijo.calculate_balance_factor()
        self.rotation_right(element, element.get_left())

    def r_root_left(self, element, hijo):
        node = BinaryTree(element.get_root(), element.get_stored_value())
        node.set_left(element.get_left())
        if element.get_left() is not None:
            element.get_left().set_higher(node)
        self.root = hijo.get_root()
        if hijo.get_left() is not None:
            node.set_right(hijo.get_left())
            hijo.get_left().set_higher(node)
        else:
            node.set_right(None)
        node.set_higher(self)
        self.left_tree = node
        self.right_tree = hijo.get_right()
        self.stored_value = hijo.get_stored_value()
        self.recalculate_balance_factor(node)

    def r_root_right_left(self, element, hijo):
        hijo.get_left().set_higher(element)
        hijo.get_left().set_right(hijo)
        self.right_tree = hijo.get_left()
        hijo.set_higher(hijo.get_left())
        hijo.set_left(None)
        hijo.calculate_balance_factor()
        self.r_root_left(element, element.get_right())

    def r_root_right(self, element, hijo):
        node = BinaryTree(element.get_root(), element.get_stored_value())
        node.set_right(element.get_right())
        if element.get_right() is not None:
            element.get_right().set_higher(node)
        self.root = hijo.get_root()
        if hijo.get_right() is not None:
            node.set_left(hijo.get_right())
            hijo.get_right().set_higher(node)
        else:
            element.set_left(None)
        self.right_tree, self.left_tree = node, hijo.get_left()
        self.stored_value = hijo.get_stored_value()
        node.set_higher(self)
        self.recalculate_balance_factor(node)


    def r_root_left_right(self, element, hijo):
        hijo.get_right().set_higher(element)
        hijo.get_right().set_left(hijo)
        self.left_tree = hijo.get_right()
        hijo.set_higher(hijo.get_right())
        hijo.set_right(None)
        hijo.calculate_balance_factor()
        self.r_root_right(element, element.get_left())

    def rotation(self, element):
        if element.get_balance_factor() == 2:
            hijo = element.get_right()
            if hijo.get_balance_factor() == 1 or hijo.get_balance_factor() == 0:
                self.rotation_left(element, hijo)
            else:
                self.rotation_right_left(element, hijo)
        else:
            hijo = element.get_left()
            if hijo.get_balance_factor() == -1 or hijo.get_balance_factor() == 0:
                self.rotation_right(element, hijo)
            else:
                self.rotation_left_right(element, hijo)

    def root_rotation(self, element):
        if element.get_balance_factor() == 2:
            hijo = element.get_right()
            if hijo.get_balance_factor() == 1 or hijo.get_balance_factor() == 0:
                self.r_root_left(element, hijo)
            else:
                self.r_root_right_left(element, hijo)
        else:
            hijo = element.get_left()
            if hijo.get_balance_factor() == -1 or hijo.get_balance_factor() == 0:
                self.r_root_right(element, hijo)
            else:
                self.r_root_left_right(element, hijo)

    def rotar(self, element):
        while element is not None and element.higher is not None:
            if abs(element.get_balance_factor()) == 2:
                self.rotation(element)
            element = element.higher
        if element is not None and abs(element.get_balance_factor()) == 2:
            self.root_rotation(element)


def main():
    bn_root = BinaryTree()
    bn_root.insert_many([
        (15, 15),
        (6, 6),
        (18, 18),
        (3, 3),
        (7, 7),
        (17, 17),
        (20, 20),
        (2, 2),
        (4, 4),
        (13, 13),
        (9, 9)
    ])

    print("==================== InOrden ====================")
    bn_root.in_order()
    in_order_value = []
    bn_root.in_order_value(in_order_value)
    print(list(map(str, in_order_value)))
    print("==================== PreOrden ====================")
    bn_root.pre_order()
    pre_order_value = []
    bn_root.pre_order_value(pre_order_value)
    print(list(map(str, pre_order_value)))
    print("==================== PostOrden ====================")
    bn_root.post_order()
    post_order_value = []
    bn_root.post_order_value(post_order_value)
    print(list(map(str, post_order_value)))
    print("==================== Search ====================")
    print(bn_root.search(2))
    print("==================== Minimum ====================")
    print(bn_root.minimum())
    print("==================== Maximum ====================")
    print(bn_root.maximum())
    print("==================== Height ====================")
    print(bn_root.get_height())
    print("==================== Mayor ====================")
    raiz = bn_root.search(3)
    print(raiz.get_higher())
    print("==================== Sucesor ====================")
    raiz = bn_root.search(3)
    print(raiz.sucesor())
    print("==================== Predecesor ====================")
    raiz = bn_root.search(3)
    print(raiz.predecesor())
    #15,6,18,3,7,17,20,2,4,13,9
    print("==================== Delete 6 ====================")
    bn_root.delete(15)
    print("==================== InOrden ====================")
    bn_root.in_order()
    in_order_value = []
    bn_root.in_order_value(in_order_value)
    print(list(map(str, in_order_value)))
    print("==================== PreOrden ====================")
    bn_root.pre_order()
    pre_order_value = []
    bn_root.pre_order_value(pre_order_value)
    print(list(map(str, pre_order_value)))
    print("==================== PostOrden ====================")
    bn_root.post_order()
    post_order_value = []
    bn_root.post_order_value(post_order_value)
    print(list(map(str, post_order_value)))

main()
