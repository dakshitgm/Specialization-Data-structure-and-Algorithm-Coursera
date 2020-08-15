# Uses python3

import sys

sys.setrecursionlimit()


def number_of_strongly_connected_components(adj):
    result = 0
    # write your code here
    def dfsanin(i):
        isVisited[i] = True
        for dest in adj[i]:
            if not isVisited[dest]:
                dfsanin(dest)
        stack.append(i)

    def dfs(i):
        isVisited[i] = False
        for dest in adjrev[i]:
            if isVisited[dest]:
                dfs(dest)

    stack = []
    isVisited = [False] * len(adj)

    for i in range(len(adj)):
        if not isVisited[i]:
            dfsanin(i)

    adjrev = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for dest in adj[i]:
            adjrev[dest].append(i)
    while len(stack):
        i = stack.pop()
        if isVisited[i]:
            dfs(i)
            result += 1
    return result


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
