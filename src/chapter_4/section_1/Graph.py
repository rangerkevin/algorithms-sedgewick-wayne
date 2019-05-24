import sys
from collections import defaultdict

class Graph:
    """The definition of graph and general APIs"""
    def __init__(self, filename=None, delimiter=None):
        self.E = 0
        self.adj = defaultdict(set)
        if filename is not None:
            fd = open(filename, 'r')
            for line in fd:
                # file object would end with ''
                if line != '':
                    # Getting rid of the new line symbol \n at the end of the line
                    line = line[:-1]
                    names = line.split(delimiter)
                    self.addEdge(names[0], names[1])

    def addEdge(self, v, w):
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.E += 1

    def vertices(self):
        return iter(self.adj)
        
    def countV(self):
        return len(self.adj)

    def countE(self):
        return self.E

    def adjacentTo(self, v):
        return iter(self.adj[v])

    def degree(self, v):
        return len(self.adjacentTo(v))

    def __str__(self):
        s = str(self.countV()) + ' vertices, ' + str(self.E) + ' edges\n'
        for v in self.vertices():
            s = s + v + ': '
            for w in self.adjacentTo(v):
                s = s + w + ' '
            s += '\n'
        return s
        

def main():
    filename = sys.argv[1]
    g = Graph(filename, ' ')
    print(g.countV())
    print(g.countE())
    print(g)

if __name__ == '__main__':
    main()
