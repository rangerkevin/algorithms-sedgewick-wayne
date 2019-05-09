class LinearProbingHashST:

    def __init__(self, M=16):
        self.M = M
        self.N = 0
        self.keys = [None] * self.M
        self.values = [None] * self.M

    def hash_(self, key):
        return (hash(key) & 0x7fffffff) % self.M

    def resize(self, cap):
        t = LinearProbingHashST(cap)
        for i in range(self.M):
            t.put(self.keys[i], self.values[i])
        self.keys = t.keys
        self.values = t.values
        self.M = t.M

    def put(self, key, val):
        if self.N >= self.M / 2:
            self.resize(2 * self.M)

        i = self.hash_(key)
        while self.keys[i] != None:
            if self.keys[i] is key:
                self.values[i] = val
                return
            i = (i + 1) % self.M

        self.keys[i] = key
        self.values[i] = val
        self.N += 1

    def get(self, key):
        i = self.hash_(key)
        while self.keys[i] != None:
            if self.keys[i] is key:
                return self.values[i]
            i = (i + 1) % self.M
        return None
    
    def contains(self, key):
        i = self.hash_(key)
        while self.keys[i] != None:
            if self.keys[i] is key:
                return True
            i = (i + 1) % self.M
        return False

    def delete(self, key):
        if not self.contains(key):
            return
        i = self.hash_(key)
        while self.keys[i] != key:
            i = (i + 1) % self.M
        self.keys[i] = None
        self.values[i] = None
        i = (i + 1) % self.M
        while self.keys[i] != None:
            keyToRedo = self.keys[i]
            valToRedo = self.values[i]
            self.keys[i] = None
            self.values[i] = None
            self.N -= 1
            self.put(keyToRedo, valToRedo)
            i = (i + 1) % self.M
        self.N -= 1
        if self.N > 0 and self.N == int(self.M / 8):
            self.resize(int(self.M / 2))

def main():
    st = LinearProbingHashST(16)
    items = [(0, 'kevin'), (1, 'sun'), (2, 'ru'), (3, 'song'), (4, 'kai'), (5, 'ryan'), (6, 'winter')]
    for key, value in items:
        st.put(key, value)
    st.delete(1)
    print(st.get(1))
    print(st.get(2))

if __name__ == '__main__':
    main()
