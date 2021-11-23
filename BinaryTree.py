# Node is one of: [ () * / + -] or number between [0,99999]


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
