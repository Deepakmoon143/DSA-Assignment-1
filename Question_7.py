def prefix_to_infix(prefix_expression):
    stack = []
    operators = set(['+', '-', '*', '/'])
    tokens = prefix_expression.split()
    
    for token in reversed(tokens):
        if token in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix_expression = f"({operand1} {token} {operand2})"
            stack.append(infix_expression)
        else:
            stack.append(token)
    
    if len(stack) == 1:
        return stack[0]
    else:
        return "Invalid Prefix Expression"


prefix_expression = input("Enter a prefix expression (eg: + * A B - C D): ")


infix_expression = prefix_to_infix(prefix_expression)
print("Infix expression:", infix_expression)
