from Stack import *


class EvaluatePostFix:
    def __init__(self):
        self.stack = Stack()
        self.OPERATORS = set(['+', '-', '*', '/'])
        

    def evaluate_posfix(self, expression):
        if len(expression) == 0:
            return str(self.stack.pop())

        if expression[0] not in self.OPERATORS: 
            self.stack.push(expression[0])
            self.evaluate_posfix(expression[1:])
        else: 
            first_operand = self.stack.pop()
            second_operand = self.stack.pop()

            if expression[0] == '+':
                result = first_operand + second_operand
            elif expression[0] == '-':
                result = first_operand - second_operand
            elif expression[0] == '*':
                result = first_operand * second_operand
            elif expression[0] == '/':
                result = first_operand / second_operand

            self.evaluate_posfix(expression[1:])
    