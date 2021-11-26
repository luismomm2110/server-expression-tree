class BinaryTree():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def create_tree_from_tokens(token_list):
        tree = BinaryTree('')
        stack = []
        stack.append(tree)
        current_tree = tree

        for i in token_list:
            if not is_operator(i):
                current_tree.left = ''
                stack.append(current_tree)
                current_tree = current_tree.left

        return tree

    def is_operator(token):
        operator = ["+", "-", "*", "-"]
        return token in operator