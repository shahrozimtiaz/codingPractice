import math


class Graph:
    class Vertex:
        def __init__(self,value):
            self.value = value
            self.adjacent = []

    def __init__(self,graph):
        self.V = len(graph)
        self.vertices = []
        for r in range(self.V):
            vertex = self.Vertex(r)
            for c in range(self.V):
                if graph[r][c]:
                    vertex.adjacent.append(c)
            self.vertices.append(vertex)
        self.graph = graph

    def dijkstra(self,src):
        dist = [math.inf] * self.V
        dist[src] = 0
        parent = [-1] * self.V
        queue = {}
        for v in self.vertices:
            queue[v.value] = v
        while queue:
            u = self.__minDistance(dist,queue)
            if u == -1:
                for v in range(self.V):
                    if dist[v] == math.inf:
                        parent[v] = 'no path'
                break
            else:
                for v in queue.pop(u).adjacent:
                    if v in queue and dist[u] + self.graph[u][v] < dist[v]:
                        dist[v] = dist[u] + self.graph[u][v]
                        parent[v] = u
        self.__printDijkstraSolution(src,dist,parent)

    def __minDistance(self,dist,queue):
        minIndex = -1
        min = math.inf
        for v in queue.keys():
            if dist[v] < min:
                minIndex = v
                min = dist[v]
        return minIndex

    def __printDijkstraSolution(self,src,dist,parent):
        for v in range(len(dist)):
            if v != src:
                if dist[v] != math.inf:
                    vs = []
                    vs.append(v)
                    p = parent[v]
                    while p != -1:
                        vs.append(p)
                        p = parent[p]
                    vs.reverse()
                    path = ''
                    for i in range(len(vs)):
                        path += str(vs[i])
                        if i < len(vs)-1:
                            path += '->'
                    print('vertex {} -> {}| Distance: {}, Path: {}'.format(src,v,dist[v],path))
                else:
                    print('vertex {} -> {}| Distance: {}, Path: {}'.format(src,v,dist[v],parent[v]))


if __name__ == '__main__':
    g = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2, 0],
        [0, 0, 7, 0, 9, 14, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6, 0],
        [8, 11, 0, 0, 0, 0, 1, 0, 7, 0],
        [0, 0, 2, 0, 0, 0, 6, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    graph = Graph(g)
    graph.dijkstra(0)
