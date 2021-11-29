import re


class CheckExpression:
    def __init__(self, expression):
        self.expression = expression

    def check_if_has_number_too_long(self):
        pattern = re.compile(r"\d{6,}")

        if pattern.match(self.expression) is None:
            return False
        else:
            return True

    def check_if_has_more_than_single_parentheses(self):
        pattern = re.compile(r"\(\(")

        if pattern.match(self.expression) is None:
            return False

        return True