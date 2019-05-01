from exercise_2 import SeparateChainingHashST

class HashTable(SeparateChainingHashST):

    def delete(self, key):
        self.st[self.hash_(key)].delete(key)


def main():
    sc = HashTable(3)
    items = [(0, 'kevin'), (1, 'sun'), (2, 'ru'), (3, 'song'), (4, 'kai'), (5, 'ryan'), (6, 'winter')]
    for item in items:
        sc.put(item[0], item[1])
    for i in range(0, 10):
        print(sc.get(i))
    sc.delete(1)
    for i in range(0, 10):
        print(sc.get(i))

if __name__ == '__main__':
    main()
