import re


class CheckExpression:
    def __init__(self, expression):
        self.expression = expression

    def validate_expression(self):
        return (self._check_if_has_only_number_with_five_digits
                and self._check_if_has_wrong_characters and
                self._check_if_ends_with_number_or_number_and_open_parentheses
                and self._check_if_has_not_operators_in_sequence
                and self._check_if_has_not_operators_in_sequence)

    def _check_if_has_wrong_characters(self):
        pattern = re.compile(r"^[\d\+\-\/\*\)\(]*$")

        return pattern.match(self.expression)

    def _check_if_ends_with_number_or_number_and_open_parentheses(self):

        pattern = re.compile(r"^.*\d\){0,1}$")

        return pattern.match(self.expression)

    def _check_if_with_starts_with_number_or_open_parenteses(self):
        pattern = re.compile(r"^\({0,1}\d.*$")

        return pattern.match(self.expression)

    def _check_if_has_not_operators_in_sequence(self):
        pattern = re.compile(r"[\+\*\/\-]{2,}")

        return pattern.match(self.expression)

    def _check_if_has_only_number_with_five_digits(self):
        pattern = re.compile(r"\d{6,}")

        return not pattern.match(self.expression)