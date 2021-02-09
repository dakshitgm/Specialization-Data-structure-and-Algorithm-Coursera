# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def inorder(root, result, key, left, right):
    if root == -1:
        return
    inorder(left[root], result, key, left, right)
    result.append(key[root])
    inorder(right[root], result, key, left, right)


def preorder(root, result, key, left, right):
    if root == -1:
        return
    result.append(key[root])
    preorder(left[root], result, key, left, right)
    preorder(right[root], result, key, left, right)


def postorder(root, result, key, left, right):
    if root == -1:
        return
    postorder(left[root], result, key, left, right)
    postorder(right[root], result, key, left, right)
    result.append(key[root])


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        inorder(0, result, self.key, self.left, self.right)

        return result

    def preOrder(self):
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        preorder(0, result, self.key, self.left, self.right)
        return result

    def postOrder(self):
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        postorder(0, result, self.key, self.left, self.right)
        return result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
