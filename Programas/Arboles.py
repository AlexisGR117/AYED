# Implementación recursiva
class BinaryTree:
    def __init__(self, value = None, stored_value = None):
        self.root = value
        self.stored_value = stored_value
        self.left_tree = None
        self.right_tree = None
        self.balance_factor = 0

    def get_root(self):
        return self.root

    def get_stored_value(self):
        return self.stored_value

    def get_left(self):
        return self.left_tree

    def get_right(self):
        return self.right_tree

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

    def __str__(self):
        return "Leaf(" + str(self.root) + ", " + str(self.stored_value) + ", " + str(self.balance_factor) + ')'

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
            return self.stored_value
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
                    self.set_right(BinaryTree(key, value))
            else:
                if self.left_tree is not None:
                    self.left_tree.insert(key, value)
                else:
                    self.set_left(BinaryTree(key, value))
        else:
            self.root, self.stored_value = key, value
        self.calculate_balance_factor()

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


main()
