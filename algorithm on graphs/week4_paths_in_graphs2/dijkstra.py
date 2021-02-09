# Uses python3

import sys
import queue
import math


class priority_queue:
    def __init__(self, distance):
        self.que = []
        self.length = 0
        self.distance = distance

    def insert(self, key):
        try:
            self.heapup(self.que.index(key))
        except ValueError:
            self.que.append(key)
            self.heapup(self.length)
            self.length += 1

    def poph(self):
        if self.length <= 0:
            return
        self.que[0], self.que[-1] = self.que[-1], self.que[0]
        key = self.que.pop()
        self.length -= 1
        self.heapify(0)
        return key

    def heapup(self, i):
        parent = math.ceil(i / 2) - 1
        while (
            self.distance[self.que[parent]] > self.distance[self.que[i]] and parent >= 0
        ):
            self.que[i], self.que[parent] = self.que[parent], self.que[i]
            i = parent
            parent = math.ceil(i / 2) - 1

    def heapify(self, i):
        left = i * 2 + 1
        right = i * 2 + 2
        smallest = i
        if (
            left < self.length
            and self.distance[self.que[smallest]] > self.distance[self.que[left]]
        ):
            smallest = left
        if (
            right < self.length
            and self.distance[self.que[smallest]] > self.distance[self.que[right]]
        ):
            smallest = right
        if smallest != i:
            que[i], que[smallest] = que[smallest], que[i]
            self.heapify(smallest)


def distance(adj, cost, s, t):
    # write your code here
    isspt = [False] * len(adj)
    distan = [float("inf")] * len(adj)
    distan[s] = 0
    df = priority_queue(distan)
    df.insert(s)
    while df.length > 0:
        source = df.poph()
        isspt[source] = True
        for dest in range(len(adj[source])):
            if (
                not isspt[adj[source][dest]]
                and distan[source] + cost[source][dest] < distan[adj[source][dest]]
            ):
                distan[adj[source][dest]] = distan[source] + cost[source][dest]
                df.insert(adj[source][dest])

    return distan[t] if distan[t] != float("inf") else -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
