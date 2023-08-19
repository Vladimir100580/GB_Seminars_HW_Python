# Программа для построения бинарного дерева и простейших операций с узлами.

class Node:
    ''' Класс для представления узла
    ...
    Атрибуты
    --------
    val : int
        значение в узле
    self.left : Node
        левый потомок
    self.right : Node
        правый потомок
    '''
    def __init__(self, val: int) -> None:
        # Устанавливает все необходимые атрибуты для объекта Node.
        self.val = val
        self.left = self.right = None


class Tree:
    # Класс бинарного дерева и работы с ним
    def __init__(self):
        # объявляем указатель root
        self.root = None

    def find(self, node: Node, parent: Node, value: int) -> tuple[None, Node, bool] | tuple[Node, Node, bool] | None:
        # Метод поиска узла по значению
        if node is None:
            return None, parent, False

        if value == node.val:
            return node, parent, True

        if value < node.val:
            if node.left:
                return self.find(node.left, node, value)

        if value > node.val:
            if node.right:
                return self.find(node.right, node, value)

        return node, parent, False

    def append(self, obj: Node) -> Node:
        # Метод добавления узла в дерево
        if self.root is None:
            self.root = obj
            return obj
        s, p, fl_find = self.find(self.root, None, obj.val)
        if not fl_find and s:
            if obj.val < s.val:
                s.left = obj
            else:
                s.right = obj

        return obj

    def print_tree(self, node: Node) -> None:
        # Печать узлов дерева слева направо (т.е. от меньшего к большему по значению узлу)
        if node is None:
            return

        self.print_tree(node.left)
        print(node.val)
        self.print_tree(node.right)

    def print_wide_tree(self, node: Node) -> None:
        # Распечатка дерева "по слоям", т.е. по степени "погружения" от главного узла.
        if node is None:
            return
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.val, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    def del_leaf(self, s: Node, p: Node) -> None:
        # Метод удаления листа (т.е. узла не имеющего потомков)
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def del_one_child(self, s: Node, p: Node) -> None:
        # метод удаления узла с одним потомком
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right in None:
                p.left = s.left
        if p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right in None:
                p.right = s.left

    def find_min(self, node: Node, parent: Node) -> tuple[Node, Node] | None:
        # Метод нахождения минимального узла и его родителя в рассматриваемой ветке.
        if node.left:
            return self.find_min(node.left, node)

        return node, parent

    def del_node(self, del_val: int) -> None:
        # Метод удаления узла (общий)
        s, p, fl_find = self.find(self.root, None, del_val)

        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.del_one_child(s, p)
        else:
            sr, pr = self.find_min(s.right, s)
            s.val = sr.val
            self.del_one_child(sr, pr)

v = [22, 5, 27, 3, 17, 12, 19, 23, 30]

t = Tree()
for x in v:
    t.append(Node(x))
t.print_wide_tree(t.root)
print("*************")
t.del_node(5)
t.print_wide_tree(t.root)

