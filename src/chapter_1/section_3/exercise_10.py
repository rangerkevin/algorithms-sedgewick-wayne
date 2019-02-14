class InfixToPostfix:
    """Exercise 1.3.10 of Algorithms Fourth Edition"""
    """General infix to postfix expression filter"""

    def __init__(self, expression):
        self.s = expression.split(' ')
        self.operators = []
        self.precedence = {'+': 1,
                           '-': 1,
                           '*': 2,
                           '/': 2}

    def getPostfixExpression(self):
        result = ''
        i = 0
        while i < len(self.s):
            cur = self.s[i]
            if cur.isdigit():
                # if digits, print to result directly
                result += cur
                i += 1
            elif cur in self.precedence:
                # if operator, compare with the peek in self.operators and pop those with higher or equal precedence
                # append the popped operators to the result output
                if len(self.operators) != 0:
                    while len(self.operators) != 0 and self.precedence[self.operators[-1]] >= self.precedence[cur]:
                        result += self.operators.pop()
                self.operators.append(cur)
                i += 1
            elif cur == '(':
                # append left parentheses to self.operators
                self.operators.append(cur)
                i += 1
            else:
                # if right parentheses, pop and append operators popped from self.operators until seen left parentheses
                last_op = self.operators[-1]
                while len(self.operators) != 0 and self.operators[-1] != '(':
                    result += self.operators.pop()
                self.operators.pop()
                i += 1
        while len(self.operators):
            # pop and append any operators left in the stack
            result += self.operators.pop()
        return result


postfix = InfixToPostfix('1 * 2 + 3 * 4')
print(postfix.s)
print(postfix.getPostfixExpression())
