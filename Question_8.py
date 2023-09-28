def brackets_balanced(code):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for i in code:
        if i in '({[':
            stack.append(i)
        elif i in ')}]':
            if not stack or stack[-1] != bracket_pairs[i]:
                return False
            stack.pop()

    return len(stack) == 0


code_snippet = input("Enter a code snippet: ")

if brackets_balanced(code_snippet):
    print("All brackets are closed and balanced.")
else:
    print("Brackets are not closed and balanced.")
