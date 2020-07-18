# python3

import sys
import threading


def compute_height(n, parents):
    # Replace this code with a faster implementation
    pars=[0]*n
    max_height = 1
    for vertex in range(n):
        if parents[vertex]!=-1:
            pars[parents[vertex]] += 1
    for vertex in range(n):
        if pars[vertex]:
            max_height+=1
    
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
