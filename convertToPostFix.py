from Stack import *
import re


class ConvertorToPosfix:
    def __init__(self, token_list):
        self.stack = Stack()
        self.output = []
        self.operators = ["+", "-", "*", "/"]
        self.precedence = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
        self.token_list = token_list

    def _check_if_is_number(self, token):
        return bool(re.search(r'\d', token))

    def _handle_unary_operator_neg(self, input_list):
        if input_list[0] == "-":
            input_list[1] = "-" + input_list[1]
            input_list.pop(0)

        for i in range(len(input_list)):
            print(i)
            if input_list[i] == "-" and input_list[i-1] in self.precedence.keys():
                input_list[i+1] = "-" + input_list[i+1]
                input_list.pop(i)

        return(input_list)

    def _process_subexpression(self):
        top_token = self.stack.pop()
        while top_token != '(':
            self.output.append(top_token)
            top_token = self.stack.pop()

    def translate_infix_to_posfix(self):
        self.token_list = self._handle_unary_operator_neg(self.token_list)

        for token in self.token_list:
            if self._check_if_is_number(token) or "." in token:
                self.output.append(token)
            elif token == '(':
                self.stack.push(token)
            elif token == ')':
                self._process_subexpression()
            else:
                while (not self.stack.empty()) and (
                        self.precedence[self.stack.peek()] >=
                        self.precedence[token]):
                    self.output.append(self.stack.pop())
                self.stack.push(token)

        while not self.stack.empty():
            self.output.append(self.stack.pop())

        return self.output
