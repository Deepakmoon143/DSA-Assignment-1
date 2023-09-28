class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def find_smallest(self):
        if self.is_empty():
            return None

        smallest = self.peek()
        for i in self.items:
            if i < smallest:
                smallest = i
        return smallest


stack = Stack()

input_str = input("Enter elements to push onto the stack (space-separated): ")
elements = input_str.split()

for i in elements:
    stack.push(int(i))


smallest = stack.find_smallest()

if smallest is not None:
    print("Smallest number in the stack:", smallest)
else:
    print("The stack is empty.")
