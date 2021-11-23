import re


class CheckExpression:
    def __init__(self, expression):
        self.expression = expression

    def check_if_has_wrong_characters(self):
        pattern = re.compile(r"[\d\+\-\/\*\)\(]{1,}")

        return pattern.search(self.expression)

    def check_if_has_only_number_with_five_digits(self):
        pattern = re.compile(r"\d{6,}")

        return pattern.match(self.expression)

    def check_if_has_only_a_single_parentheses(self):
        pattern = re.compile(r"\(\(")

        return pattern.match(self.expression)