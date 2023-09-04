class Tree:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.data}"


def insert(node: Tree, data: int) -> None:
    into = []
    into.append(node)
    while len(into):
        node = into[0]
        into.pop(0)
        if node.left == None:
            if data != None:
                node.left = Tree(data)
            else:
                node.left = Tree(None)
            break
        else:
            into.append(node.left)
        if node.right == None:
            if data != None:
                node.right = Tree(data)
            else:
                node.right = Tree(None)
            break
        else:
            into.append(node.right)


def make_tree(elements: list) -> Tree:
    binary_tree = Tree(elements[0])
    for i in elements[1:]:
        insert(binary_tree, i)
    return binary_tree


class Solution:
    def maxpath(self, root):
        self.answer = -float("inf")
        self.solve(root)
        return self.answer

    def solve(self, node):
        if node == None or node.stations == None:
            return 0
        left = max(0, self.solve(node.left))
        right = max(0, self.solve(node.right))
        self.answer = max(self.answer, left + right + node.stations)
        return node.stations + max(left, right)


Obj = Solution()
t = make_tree([-10, 9, 10, None, None, 15, 7])
print(Obj.maxpath(t))
