from Graph import Graph
import sys

class Cycle:
    """
    Determining if a graph has cycle
    """

    def __init__(self, G):
        self.marked = {}
        self.hasCycle = False
        for v in G.vertices():
            self.marked[v] = False
        for v in G.vertices():
            if not self.marked[v]:
                self.dfs(G, v, v)

    def dfs(self, G, v, u):
        self.marked[v] = True
        for w in G.adjacentTo(v):
            if not self.marked[w]:
                self.dfs(G, w, v)
            elif w != u:
                # Adding w != u could eliminate the case that a vertex has parallel edges
                # For example A has two edges connecting to B
                # By default this scenario is not considerred as having cycle in a graph
                self.hasCycle = True

    def hasCycle(self):
        return self.hasCycle

def main():
    filename = sys.argv[1]
    g = Graph(filename, ' ')
    detectCycle = Cycle(g)
    print('Does this graph has cycle: ' + str(detectCycle.hasCycle))

if __name__ == '__main__':
    main()
