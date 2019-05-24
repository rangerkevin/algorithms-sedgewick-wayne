from Graph import Graph
import sys

class DepthFirstSearch:
    """The public class for depth first search"""
    def __init__(self, G, s):
        self.marked = {}
        self.count = 0
        # Initializing the marked dictionary
        for v in G.vertices():
            self.marked[v] = False
        self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = True
        self.count += 1
        for w in G.adjacentTo(v):
            if not self.marked[w]:
                self.dfs(G, w)

    def isMarked(self, v):
        return self.marked[v]

    def getCount(self):
        return self.count


def main():
    filename = sys.argv[1]
    g = Graph(filename, ' ')
    search = DepthFirstSearch(g, 'X')
    search.dfs(g, 'X')
    print(g.adj)
    print(search.marked)
    print(search.getCount())

if __name__ == '__main__':
    main()
