class StackIterator:
    """Exercise 1.3.12 of Algorithms Fourth Edition"""

    def __init__(self, stack):
        self.stack = stack
        
    def hasNext(self):
        return len(self.stack) != 0

    def next(self):
        if self.hasNext():
            return self.stack.pop()

class CopyStack:

    def __init__(self, iterator):
        self.iterator = iterator

    def copy(self):
        temp = []
        result = []

        while self.iterator.hasNext():
            temp.append(self.iterator.next())

        temp = StackIterator(temp)

        while temp.hasNext():
            result.append(temp.next())

        return result


stack = [1, 2, 3]
result = CopyStack(StackIterator(stack))
print(result.copy())
            
