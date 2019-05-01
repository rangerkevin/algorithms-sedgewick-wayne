from SequentialSearchST import *

class SeparateChainingHashST:

    def __init__(self, M):
        self.M = M
        self.st = [None] * M
        for i in range(M):
            self.st[i] = SequentialSearchST()

    def hash_(self, key):
        """Use Python hash() as hashCode()"""
        return (hash(key) & 0x7fffffff) % self.M

    def get(self, key):
        return self.st[self.hash_(key)].get(key)

    def put(self, key, val):
        self.st[self.hash_(key)].put(key, val)

def main():
    sc = SeparateChainingHashST(3)
    items = [(0, 'kevin'), (1, 'sun'), (2, 'ru'), (3, 'song'), (4, 'kai'), (5, 'ryan'), (6, 'winter')]
    for item in items:
        sc.put(item[0], item[1])
    for i in range(0, 10):
        print(sc.get(i))

if __name__ == '__main__':
    main()
