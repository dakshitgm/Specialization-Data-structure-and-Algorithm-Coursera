#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 8)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    def isvalid(root, Max_num, min_num):
        if tree[root][0] < Max_num and tree[root][0] > min_num:
            return (
                tree[root][1] == -1 or isvalid(tree[root][1], tree[root][0], min_num)
            ) and (
                tree[root][2] == -1 or isvalid(tree[root][2], Max_num, tree[root][0])
            )
        return False

    if len(tree) < 2:
        return True
    return (tree[0][1] == -1 or isvalid(tree[0][1], tree[0][0], -float("inf"))) and (
        tree[0][2] == -1 or isvalid(tree[0][2], float("inf"), tree[0][0])
    )
    return False


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
