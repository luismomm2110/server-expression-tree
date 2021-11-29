from pdb import set_trace
from Stack import *


class EvaluatePostFix:
    def __init__(self, expression):
        self.stack = Stack()
        self.expression = expression
        self.OPERATORS = set(['+', '-', '*', '/'])

    def evaluate_posfix(self):
        if len(self.expression) == 0:
            return str(float(self.stack.peek()))

        if self.expression[0] not in self.OPERATORS:
            self.stack.push(self.expression[0])
            self.expression = self.expression[1:]
            return self.evaluate_posfix()
        else:
            first_operand = float(self.stack.pop())
            second_operand = float(self.stack.pop())

            if self.expression[0] == '+':
                result = first_operand + second_operand
            elif self.expression[0] == '-':
                result = second_operand - first_operand
            elif self.expression[0] == '*':
                result = first_operand * second_operand
            elif self.expression[0] == '/':
                result = second_operand / first_operand

            self.stack.push(result)
            self.expression = self.expression[1:]

            return self.evaluate_posfix()
