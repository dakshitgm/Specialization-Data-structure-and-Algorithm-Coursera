# Uses python3
from collections import deque
import sys
import queue


def distance(adj, s, t):
    # write your code here
    distance = [-1] * len(adj)
    distance[s] = 0
    verque = deque()
    verque.append(s)
    while len(verque) > 0:
        vertex = verque.popleft()
        for dest in adj[vertex]:
            if distance[dest] == -1:
                verque.append(dest)
                distance[dest] = distance[vertex] + 1
            if dest == t:
                break
    return distance[t]


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
