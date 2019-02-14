class InfixExpression:
    """Exercise 1.3.9 of Algorithms Fourth Edition"""

    def __init__(self, expression):
        self.expression = expression

    def getInfixExpression(self):
        operands = []
        operators = []
        expression = ''
        for i in range(len(self.expression)):
            if self.expression[i] == '(' or self.expression[i] == ' ':
                continue
            elif self.expression[i] in ['+', '-', '*', '/']:
                operators.append(self.expression[i])
            elif self.expression[i] == ')':
                value2 = operands.pop()
                value1 = operands.pop()
                op = operators.pop()
                operands.append('(' + value1 + ' ' + op + ' ' + value2 + ')')
            else:
                num = ''
                while i < len(self.expression) and self.expression[i].isdigit():
                    num += self.expression[i]
                    i += 1
                operands.append(num)
        return operands.pop()


infix = InfixExpression('1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )')
print infix.getInfixExpression()
