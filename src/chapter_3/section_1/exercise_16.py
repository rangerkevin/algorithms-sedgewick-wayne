class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class BinarySearchST:

    def __init__(self, itemList):
        self.capacity = len(itemList)
        self.items = itemList
        self.sort()

    def sort(self):
        aux = list(self.items)
        self.sort_helper(aux, 0, self.capacity - 1)

    def sort_helper(self, aux, start, end):
        if start >= end:
            return
        mid = int((start + end) / 2)
        self.sort_helper(aux, start, mid)
        self.sort_helper(aux, mid + 1, end)
        if self.items[mid].key <= self.items[mid + 1].key:
            return
        self.merge(aux, start, mid, end)

    def merge(self, aux, start, mid, end):
        i, j = start, mid + 1

        for k in range(start, end + 1):
            if i > mid:
                self.items[k] = aux[j]
                j += 1
            elif j > end:
                self.items[k] = aux[i]
                i += 1
            elif aux[i].key < aux[j].key:
                self.items[k] = aux[i]
                i += 1
            else:
                self.items[k] = aux[j]
                j += 1

    def size(self):
        return self.capacity

    def get(self, key):
        if self.isEmpty():
            return None
        index = self.rank(key)
        if index < self.capacity and self.items[index].key == key:
            return self.items[index].value
        return None    

    def isEmpty(self):
        return self.capacity == 0

    def rank(self, key):
        start, end = 0, self.capacity - 1
        while start <= end:
            mid = int((start + end) / 2)
            midKey = self.items[mid].key
            if midKey == key:
                return mid
            elif midKey < key:
                start = mid + 1
            else:
                end = mid - 1
        return start

    def put(self, key, value):
        index = self.rank(key)
        if index < self.capacity and self.items[index].key == key:
            # Found match and update
            self.items[index].value = value
            return
        # Not found and now moving all items after index to the right for 1 unit
        self.items.append(Item(None, None))
        for i in range(self.capacity, index, -1):
            self.items[i] = self.items[i - 1]
        self.items[index] = Item(key, value)
        self.capacity += 1

    def delete(self, key):
        index = self.rank(key)
        if index < self.capacity and self.items[index].key == key:
            # delete
            for i in range(index, self.capacity - 1):
                self.items[i] = self.items[i + 1]
            self.capacity -= 1
            return self.items.pop().key
        else:
            return None      



        

key_val_pairs = []
i = 100
while i > 0:
    key_val_pairs.append(tuple([i, i - 1]))
    i -= 2
itemList = []
for i in range(len(key_val_pairs) - 1, -1, -1):
    item = key_val_pairs[i]
    itemList.append(Item(item[0], item[1]))
st = BinarySearchST(itemList)
print(st.size())
print(st.isEmpty())
print(st.get(1))
print(st.get(2))
print(st.get(3))
print(st.get(100))
print(st.put(100, 1234))
print(st.put(102, 101))
print(st.delete(102))
print(st.delete(102))
