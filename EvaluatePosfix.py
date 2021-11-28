from Stack import *


class EvaluatePostFix:
    def __init__(self, expression):
        self.stack = Stack()
        self.OPERATORS = set(['+', '-', '*', '/'])
        self.expression = expression

    def evaluate_posfix(self):
        if len(self.expression) == 0:
            return str(self.stack.peek())

        if self.expression[0] not in self.OPERATORS:
            self.stack.push(self.expression[0])
            self.expression = self.expression[1:]
            return self.evaluate_posfix()
        else:
            first_operand = int(self.stack.pop())
            second_operand = int(self.stack.pop())

            if self.expression[0] == '+':
                result = first_operand + second_operand
            elif self.expression[0] == '-':
                result = second_operand - first_operand
            elif self.expression[0] == '*':
                result = first_operand * second_operand
            elif self.expression[0] == '/':
                result = second_operand / first_operand
            self.expression = self.expression[1:]
            self.stack.push(result)

            return self.evaluate_posfix()
