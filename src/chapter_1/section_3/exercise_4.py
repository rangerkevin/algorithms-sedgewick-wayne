class validParentheses:
    """Problem 1.3.4 of Algorithms Fourth Edition, page 102"""

    def __init__(self, s):
        self.s = s
        self.stack = []

    def isBalanced(self):
        for c in self.s:
            if c == '(' or c == '[' or c == '{':
                self.stack.append(c)
            else:
                if len(self.stack) == 0:
                    return False
                if c == ')' and self.stack.pop() != '(':
                    return False
                if c == ']' and self.stack.pop() != '[':
                    return False
                if c == '}' and self.stack.pop() != '{':
                    return False
        return len(self.stack) == 0

s = '()([{}]){}{'
p = validParentheses(s)
print p.isBalanced()
