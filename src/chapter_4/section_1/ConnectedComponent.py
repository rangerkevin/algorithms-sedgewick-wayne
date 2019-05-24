import sys
from Graph import Graph

class ConnectedComponent:
    """The connected component class for detecting the connected components in the graph"""
    def __init__(self, G):
        self.marked = {}
        self.id = {}
        self.count = 0
        for v in G.vertices():
            self.marked[v] = False
        for v in G.vertices():
            if not self.marked[v]:
                self.dfs(G, v)
                self.count += 1

    def dfs(self, G, v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in G.adjacentTo(v):
            if not self.marked[w]:
                self.dfs(G, w)

    def connected(self, v, w):
        return self.id[v] == self.id[w]

    def getId(self, v):
        return self.id[v]
        
    def getCount(self):
        return self.count 


def main():
    filename = sys.argv[1]
    s = sys.argv[2]
    d = sys.argv[3]
    g = Graph(filename, ' ')
    cc = ConnectedComponent(g)
    print(cc.getCount())
    print('Is ' + s + ' connected to ' + d + ': ' + str(cc.connected(s, d)))

if __name__ == '__main__':
    main()
