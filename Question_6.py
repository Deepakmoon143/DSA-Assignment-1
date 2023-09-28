def postfix_to_prefix(postfix_expression):
    stack = []

    for i in postfix_expression:
        if i.isalnum():
            stack.append(i)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix_expression = i + operand1 + operand2
            stack.append(prefix_expression)

    if len(stack) == 1:
        return stack[0]
    else:
        return "Invalid postfix expression"


postfix_expression = input("Enter a postfix expression: ")


result = postfix_to_prefix(postfix_expression)


print("Prefix expression:", result)
