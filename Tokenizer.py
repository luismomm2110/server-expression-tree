def token_expressions(expression):
    builtin_tokens = ['(', ')', '+', '-', '*', '/']
    parsed_tokens = []
    number = ""
    before_dot = ""

    for char in expression:
        if char in builtin_tokens:
            parsed_tokens.append(number)
            parsed_tokens.append(char)
            number = ''
        elif char == '.':
            parsed_tokens.append(number)
            number = ''
            before_dot = parsed_tokens.pop() + char
        else:
            number = before_dot + number + char
            before_dot = ""

    parsed_tokens.append(number)
    parsed_tokens = list(filter(None, parsed_tokens))

    return parsed_tokens
