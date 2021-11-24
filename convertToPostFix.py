class ConvertorToPostfix:
    def __init__(self):
        self.top = -1
        self.stack = []
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def is_empty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.stack.pop()
        else:
            return "$"

    def push(self, token):
        self.top += 1
        self.stack.append(token)

    def is_operand(self, token):
        return token.isalpha()  # ???

    def not_greater_precedence(self, token):
        try:
            a = self.precedence[token]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    def find_precendent_parentheses_in_stack(self):
        while ((not self.is_empty()) and self.peek() != '('):
            a = self.pop()
            self.output.append(a)
            if (not self.isEmpty() and self.peek() != '('):
                return -1
            else:
                self.pop()

    def translate_infix_to_postfix(self, infix_tokens):
        for token in infix_tokens:
            if self.is_operand(token):
                self.output.append(token)

            elif token == '(':
                self.push(token)

            elif token == ')':
                self.find_precendent_parentheses_in_stack()

            else:
                while (not self.is_empty()
                       and self.not_greater_precedence(token)):
                    self.output.append(self.pop())
                self.push(token)

        while not self.is_empty():
            self.output.append(self.pop())

        return self.output