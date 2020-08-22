# Uses python3
import sys
import queue


def bipartite(adj):
    # write your code here
    isbiparatite = True
    colour = [None] * len(adj)
    verque = queue.Queue()
    for source in range(len(adj)):
        if colour[source] != float("inf"):
            continue
        verque.put(source)
        colour[source] = True
        while not verque.empty():
            vertex = verque.get()
            for neighbours in adj[vertex]:
                if colour[neighbours] == None:
                    verque.put(neighbours)
                    colour[neighbours] = not colour[vertex]
                elif colour[vertex] == colour[neighbours]:
                    return 0
    return 1


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
    print(bipartite(adj))
