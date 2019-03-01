class UnionFind:
    """Exercise 1.5.1 of Algorithms Fourth Edition"""

    def __init__(self, N):
        self.id = [i for i in range(N)]
        #self.rank = [1 for _ in range(N)]
        self.N = N
        self.count = N

    def find(self, p):
        return self.id[p]

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        # Assign q's id to p
        pid = self.find(p)
        qid = self.find(q)
        if pid == qid:
            return
        count = 0
        for i in range(self.N):
            if self.id[i] == pid:
                count += 1
                self.id[i] = qid
                self.count -= 1
        print(self.id)
        print(count)
        print("Number of connected components: " + str(self.count))

uf = UnionFind(10)
uf.union(9, 0)
uf.union(3, 4)
uf.union(5, 8)
uf.union(7, 2)
uf.union(2, 1)
uf.union(5, 7)
uf.union(0, 3)
uf.union(4, 2)

