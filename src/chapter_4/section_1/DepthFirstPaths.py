from Graph import Graph
import sys

class DepthFirstPaths:
    """Class for finding the path from source s to destination v"""
    def __init__(self, G, s):
        self.marked = {}
        self.s = s
        self.edgeTo = {}
        for v in G.vertices():
            self.marked[v] = False
        self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = True
        for w in G.adjacentTo(v):
            if not self.marked[w]:
                # Keeping track of the previous node to w, which is v
                self.edgeTo[w] = v
                self.dfs(G, w)

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
    g = Graph(filename, ' ')
    path = DepthFirstPaths(g, 'B')
    print('Source ' + path.s + ' has path to X: ' + str(path.hasPathTo('X')))
    print('Source ' + path.s + ' has path to G: ' + str(path.hasPathTo('G')))
    p = path.pathTo('G')
    result = 'Path: '
    while len(p) != 0:
        if result == 'Path: ':
            result = result + p.pop()
        else:
            result = result + '->' + p.pop()
    print(result)

if __name__ == '__main__':
    main()
