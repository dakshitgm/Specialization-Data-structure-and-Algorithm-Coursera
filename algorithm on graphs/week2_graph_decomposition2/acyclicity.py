# Uses python3

import sys


def acyclic(adj, n):
    isVisited = [False] * n
    isSinked = [False] * n

    def traverse(source):
        if isVisited[source]:
            return False
        isVisited[source] = True
        for dest in adj[source]:
            if not (isSinked[dest] or traverse(dest)):
                return False
        isSinked[source] = True
        return True

    for i in range(n):
        if not isVisited[i]:
            if not traverse(i):
                return 1
    return 0


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj, n))
