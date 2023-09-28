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

    def reverse(self):
        if self.size() > 0:
            item = self.pop()
            self.reverse()
            self.insert_at_bottom(item)

    def insert_at_bottom(self, item):
        if self.is_empty():
            self.push(item)
        else:
            temp = self.pop()
            self.insert_at_bottom(item)
            self.push(temp)


stack = Stack()


input_str = input("Enter elements to push onto the stack (space-separated): ")
elements = input_str.split()

for i in elements:
    stack.push(i)

print("Original Stack:", stack.items)

stack.reverse()

print("Reversed Stack:", stack.items)
