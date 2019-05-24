from Graph import Graph
from collections import deque
import sys

class BreadthFirstPaths:
    """Class for finding the shortest path from source s to destination v using BFS"""
    def __init__(self, G, s):
        self.marked = {}
        self.s = s
        self.edgeTo = {}
        for v in G.vertices():
            self.marked[v] = False
        self.bfs(G, s)

    def bfs(self, G, v):
        queue = deque([v])
        self.marked[v] = True
        while len(queue) != 0:
            n = queue.popleft()
            for w in G.adjacentTo(n):
                if not self.marked[w]:
                    queue.append(w)
                    self.marked[w] = True
                    self.edgeTo[w] = n

    def hasPathTo(self, v):
        return self.marked[v]

    def pathTo(self, v):
        if not self.marked[v]:
            return None
        path = []
        x = v
        while x != self.s:
            path.append(x)
            x = self.edgeTo[x]
        path.append(self.s)
        return path


def main():
    filename = sys.argv[1]
    source = sys.argv[2]
    destination = sys.argv[3]
    g = Graph(filename, ' ')
    print(g)
    path = BreadthFirstPaths(g, source)
    print('Source ' + source + ' has path to ' + destination + ': ' + str(path.hasPathTo(destination)))
    if path.hasPathTo(destination):
        p = path.pathTo(destination)
        result = 'Path: '
        while len(p) != 0:
            if result == 'Path: ':
                result = result + p.pop()
            else:
                result = result + '->' + p.pop()
        print(result)

if __name__ == '__main__':
    main()

    
