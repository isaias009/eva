def tokenize(expression):
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    for i, token in enumerate(tokens):
        try:
            tokens[i] = float(token)
        except ValueError:
            pass
    return tokens

def shunting_yard(tokens):
    output = []
    operators = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for token in tokens:
        if isinstance(token, (int, float)):
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()
        elif token in precedence:
            while operators and precedence.get(operators[-1], 0) >= precedence[token]:
                output.append(operators.pop())
            operators.append(token)

    while operators:
        output.append(operators.pop())

    return output

def evaluate_rpn(rpn_tokens):
    stack = []
    steps = []

    for token in rpn_tokens:
        if isinstance(token, (int, float)):
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            elif token == '^':
                result = a ** b
            stack.append(result)
            steps.append(f"{a} {token} {b} = {result}")

    return stack[0], steps

def calculate(expression):
    tokens = tokenize(expression)
    rpn_tokens = shunting_yard(tokens)
    result = evaluate_rpn(rpn_tokens)
    return result
