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