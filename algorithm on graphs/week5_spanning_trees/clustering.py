#Uses python3
import sys
import math


class disjoint_set:
    def __init__(self, n):
        self.no_set = n
        self.vertex = list(range(n))
        self.parents = list(range(n))
        self.rank = [1 for _ in range(n)]

    def union(self, v1, v2):
        v1 = self.find(v1)
        v2 = self.find(v2)
        if v1 == v2:
            return False
        if self.rank[v1] < self.rank[v2]:
            self.parents[v1] = v2
        else:
            self.parents[v2] = v1
        if self.rank[v1] == self.rank[v2]:
            self.rank[v2] += 1
        self.no_set -= 1
        return True

    def find(self, vertex):
        if self.parents[vertex] != self.parents[self.parents[vertex]]:
            self.parents[vertex] = self.find(self.parents[vertex])
        return self.parents[vertex]


def distance(x1, y1, x2, y2):
    x = (x1 - x2)**2
    y = (y1 - y2)**2
    return (x + y)**(1 / 2)


def clustering(x, y, k):
    #write your code here
    distances = []
    for i in range(len(x) - 1):
        for j in range(1, len(x)):
            distances.append([distance(x[i], y[i], x[j], y[j]), i, j])
    distances.sort(reverse=True)
    clusters = disjoint_set(len(x))
    while clusters.no_set > k:
        edge = distances.pop()
        clusters.union(edge[1], edge[2])

    while True:
        edge = distances.pop()
        if clusters.union(edge[1], edge[2]):
            return edge[0]
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
