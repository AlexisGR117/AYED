from sys import stdin


class BinaryTree:
    def __init__(self, value=None, stored_value=None):
        self.root = value
        self.stored_value = stored_value
        self.left_tree = None
        self.right_tree = None
        self.parent = None

    def get_root(self):
        return self.root

    def get_stored_value(self):
        return self.stored_value

    def get_left(self):
        return self.left_tree

    def get_right(self):
        return self.right_tree

    def get_parent(self):
        return self.parent

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

    def set_parent(self, new_tree):
        if isinstance(new_tree, BinaryTree) or new_tree is None:
            self.parent = new_tree

    def __str__(self):
        return "Leaf(" + str(self.root) + ", " + str(self.stored_value) + ')'

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

    def is_empty(self):
        return self.root is None

    def insert(self, key, value):
        if not self.is_empty():
            if key >= self.root:
                if self.right_tree is not None:
                    self.right_tree.insert(key, value)
                else:
                    new = BinaryTree(key, value)
                    new.set_parent(self)
                    self.set_right(new)
            else:
                if self.left_tree is not None:
                    self.left_tree.insert(key, value)
                else:
                    new = BinaryTree(key, value)
                    new.set_parent(self)
                    self.set_left(new)
        else:
            self.root, self.stored_value = key, value

    def insert_many(self, data=[]):
        for dat in data:
            self.insert(dat[0], dat[1])


def solve(pre_order, in_order, tree):
    if pre_order == "" and in_order == "":
        return None
    else:
        root = pre_order[0]
        tree.root = root
        tree.stored_value = root
        if len(pre_order) == 1 and len(in_order) == 1:
            return tree
        else:
            location = in_order.index(root)
            left = in_order[0:location]
            right = in_order[location + 1:]
            tree.set_left(solve(pre_order[1:len(left) + 1], left, BinaryTree()))
            tree.set_right(solve(pre_order[len(left) + 1:], right, BinaryTree()))
            return tree


def main():
    line = stdin.readline().strip()
    while line != "":
        word_1, word_2 = line.split()
        tree = BinaryTree()
        solve(word_1, word_2, tree)
        post_order_value = []
        tree.post_order_value(post_order_value)
        for i in range(len(post_order_value) - 1):
            print(post_order_value[i].get_root(), end="")
        print(post_order_value[-1].get_root())
        line = stdin.readline().strip()


main()
