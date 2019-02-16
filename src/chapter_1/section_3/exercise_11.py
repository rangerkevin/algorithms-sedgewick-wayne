from exercise_10 import *

class EvaluatePostfix:
    """Exercise 1.3.11 of Algorithms Fourth Edition"""

    def __init__(self, postfixExpression):
        self.s = postfixExpression.split(' ')
        self.operands = []

    def getResult(self):
        for c in self.s:
            if c.isdigit():
                self.operands.append(int(c))
            else:
                value2 = self.operands.pop()
                value1 = self.operands.pop()
                operator = c
                ans = self.doMath(value1, value2, operator)
                self.operands.append(ans)                
        return self.operands.pop()

    def doMath(self, value1, value2, operator):
        if operator == '+':
            return value1 + value2
        if operator == '-':
            return value1 - value2
        if operator == '*':
            return value1 * value2
        if operator == '/':
            return value1 / value2


text = '2 * 3 + 1 * 4'
print('Infix expression: ' + text)
postfix = InfixToPostfix(text)
print('Postfix expression: ' + postfix.getPostfixExpression())
test = EvaluatePostfix(postfix.getPostfixExpression())
print('Result: ' + str(test.getResult()))
