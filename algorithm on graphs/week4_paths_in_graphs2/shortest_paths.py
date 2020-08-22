# Uses python3

import sys
import queue

Infinity = 1e512


def dfs(i, adj, shortest):
    shortest[i] = 0
    for dest in adj[i]:
        if shortest[dest] != 0:
            dfs(dest, adj, shortest)


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    # write your code here
    distance[s] = 0
    for _ in range(len(adj) - 1):
        isRelaxed = False
        for source in range(len(adj)):
            for dest in range(len(adj[source])):
                if (
                    distance[source] != Infinity
                    and distance[source] + cost[source][dest]
                    < distance[adj[source][dest]]
                ):
                    distance[adj[source][dest]] = distance[source] + cost[source][dest]
                    isRelaxed = True
        if not isRelaxed:
            return

    for source in range(len(adj)):
        for dest in range(len(adj[source])):
            if (
                distance[source] != Infinity
                and distance[source] + cost[source][dest] < distance[adj[source][dest]]
                and shortest[adj[source][dest]] != 0
            ):
                dfs(adj[source][dest], adj, shortest)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(
        zip(zip(data[0 : (3 * m) : 3], data[1 : (3 * m) : 3]), data[2 : (3 * m) : 3])
    )
    data = data[3 * m :]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [Infinity] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if distance[x] == Infinity:
            print("*")
        elif shortest[x] == 0:
            print("-")
        else:
            print(distance[x])

