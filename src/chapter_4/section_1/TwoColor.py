from Graph import Graph
import sys 

class TwoColor:
    """
    Determining if a graph is bipartite
    """

    def __init__(self, G):
        self.marked = {}
        self.color = {}
        self.isTwoColorable = True
        for v in G.vertices():
            self.marked[v] = False
            self.color[v] = False
        for v in G.vertices():
            self.dfs(G, v)

    def dfs(self, G, v):
        self.marked[v] = True
        for w in G.adjacentTo(v):
            if not self.marked[w]:
                self.color[w] = not self.color[v]
                self.dfs(G, w)
            elif self.color[w] == self.color[v]:
                self.isTwoColorable = False

    def isBipartite(self):
        return self.isTwoColorable

def main():
    filename = sys.argv[1]
    g = Graph(filename, ' ')
    testTwoColor = TwoColor(g)
    print(testTwoColor.isBipartite())

if __name__ == '__main__':
    main()
