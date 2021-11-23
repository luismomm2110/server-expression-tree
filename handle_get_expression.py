import re


class CheckExpression:
    def __init__(self, expression):
        self.expression = expression

    def _check_if_has_wrong_characters(self):
        pattern = re.compile("^[\d\+\-\/\*\)\(]*$")

        return pattern.match(self.expression)

    def _check_if_ends_with_number_or_number_and_open_parentheses(self):

        pattern = re.compile("^.*\d\){0,1}$")

        return pattern.match(self.expression)

    def _check_if_with_starts_with_number_or_open_parenteses(self):
        pattern = re.compile("^\({0,1}\d.*$")

        return pattern.match(self.expression)

    def _check_if_has_not_operators_in_sequence(self):
        pattern = re.compile("[\+\*\/\-]{2,}")

        return pattern.match(self.expression)

    def _check_if_has_only_number_with_five_digits(self):
        pattern = re.compile("\d{6,}")

        return not pattern.match(self.expression)