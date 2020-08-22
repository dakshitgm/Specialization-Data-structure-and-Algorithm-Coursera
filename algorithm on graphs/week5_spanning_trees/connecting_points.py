#Uses python3
import sys
import math
import heapq
import random
def distance(x1, y1, x2, y2):
    x = (x1 - x2)** 2
    y = (y1 - y2)** 2
    return (x + y)**(1 / 2)



def minimum_distance(x, y):
    result = 0.
    #write your code here
    isConnected = [False] * len(x)
    nodes_connected=0
    start = random.randint(0, len(x)-1)
    que = []
    heapq.heappush(que, [0, start])
    while nodes_connected<len(x) or len(que)>0:
        edge = heapq.heappop(que)
        vertex = edge[1]
        if not isConnected[vertex]:
            result+=edge[0]
            isConnected[vertex] = True
            nodes_connected+=1
            for ver in range(len(x)):
                if not isConnected[ver]:
                    heapq.heappush(que, [distance(x[vertex], y[vertex], x[ver], y[ver]), ver])
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
