from Stack import *


class ConvertorToPosfix:
    def __init__(self, token_list):
        self.stack = Stack()
        self.output = []
        self.precedence = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
        self.token_list = token_list

    def _process_subexpression(self):
        top_token = self.stack.pop()
        while top_token != '(':
            self.output.append(top_token)
            top_token = self.stack.pop()

    def translate_infix_to_posfix(self):
        for token in self.token_list:
            if token.isdigit() or '.' in token:
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
