def token_expressions(expression):
    builtin_tokens = ['(', ')', '+', '-', '*', '/']
    parsed_tokens = []
    number = ""

    for char in expression:
        if char in builtin_tokens:
            parsed_tokens.append(number)
            parsed_tokens.append(char)
            number = ''
        else:
            number = number + char

    parsed_tokens.append(number)
    parsed_tokens = list(filter(None, parsed_tokens))

    return parsed_tokens
