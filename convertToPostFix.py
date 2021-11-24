class Stack:
    def __init__(self):
        self.stack = [] 

        def push(self, data):
            self.stack.append(data)

        def pop(self):
            if self.stack:
                return self.stack.pop()
            else: 
                return None

        def size(self):
            return len(self.stack)

        def empty(self):
            return True if self.size() == 0 else False 

        def peek(self):
            return self.stack[-1]

class ConvertorToPostfix:
    def __init__(self, token_list):
        self.stack = Stack()
        self.output = []
        self.precedence = {'(' : 1, '+': 2, '-': 2, '*': 3, '/': 3}
        self.token_list = token_list

    def process_subexpression(self):
                top_token = self.stack.pop()
                while top_token != '(':
                    self.output.append(top_token)
                    top_token = self.stack.pop()
                
    def translate_infix_to_postfix(self):
        for token in self.token_list:
            if token in "0123456789":
                self.output.append(token)
            elif token == '(':
                self.stack.push(token)
            elif token == ')':
                self.process_subexpression()
            else:
                while (not self.stack.empty()) and (self.precedence[self.stack.peek()] >= self.precedence[token]):
                    self.output.append(self.stack.pop())
                self.stack.push(token)

        while not self.stack.empty():
            self.output.append(self.stack.pop())

        return self.output
            
               



    