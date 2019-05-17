from exercise_2 import *
from exercise_17 import *

class SeparateChainingHashSTWithKeys(SeparateChainingHashST):

    def keys(self):
        results = []
        for st in self.st:
            for key in st.keys():
                results.append(key)
        return results

class LinearProbingHashSTWithKeys(LinearProbingHashST):

    def keyIterator(self):
        # LinearProbingHashST has an instance variable called keys already, thus naming the keys() method as keyIterator
        results = []
        for key in self.keys:
            if key == None:
                continue
            results.append(key)
        return results


def main():
    sc = SeparateChainingHashSTWithKeys(4)
    lp = LinearProbingHashSTWithKeys(16)
    items = [(0, 'kevin'), (1, 'sun'), (2, 'ru'), (3, 'song'), (4, 'kai'), (5, 'ryan'), (6, 'wint    er'), (7, 'ray'), (8, 'judy')]
    for item in items:
        sc.put(item[0], item[1])
        lp.put(item[0], item[1])

    print(sc.keys())
    print(lp.keyIterator())

if __name__ == '__main__':
    main()
