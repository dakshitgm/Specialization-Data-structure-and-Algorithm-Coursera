# python3
import queue
class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:
    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].capacity -= flow
        self.edges[id ^ 1].capacity += flow

class MaxMatching:
    def read_data(self):
        self.n, self.m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(self.n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        matching=[-1]*self.n
        graph=FlowGraph(self.n+self.m+2)
        from_=0
        to=self.n+self.m+1
        for i in range(1,self.n+1):
            graph.add_edge(from_, i, 1)
        for i in range(self.n):
            for j in range(self.m):
                if adj_matrix[i][j]==1:
                    graph.add_edge(i+1, self.n+j+1, 1)

        for i in range(self.n+1, to):
            graph.add_edge(i, to, 1)

        while True:
            qu=queue.Queue()
            qu.put(from_)
            prev=[None]*graph.size()
            prev[from_]=-1
            while not qu.empty():
                curVertex=qu.get()
                for edgeId in graph.get_ids(curVertex):
                    edge=graph.get_edge(edgeId)
                    desVertex=edge.v
                    if prev[desVertex]==None and edge.capacity>0:
                        prev[desVertex]=edgeId
                        if desVertex==to:
                            break
                        qu.put(desVertex)
            if prev[to]==None:
                break
            curEdgeId=prev[to]
            while curEdgeId>=0:
                graph.add_flow(curEdgeId, 1)
                curEdge=graph.get_edge(curEdgeId)
                if curEdge.u in range(1, self.n+1):
                    matching[curEdge.u-1]=curEdge.v-self.n

                curEdgeId=prev[curEdge.u]
        
        return matching

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
