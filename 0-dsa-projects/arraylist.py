class Stack:
    def __init__(self):
        self.data = []  # underlying array

    # PUSH → add to top
    def push(self, value):
        self.data.append(value)

    # POP → remove from top
    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()

    # PEEK → look at top
    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]

    # CHECK EMPTY
    def is_empty(self):
        return len(self.data) == 0

    # SIZE
    def size(self):
        return len(self.data)

    # PRINT (debugging)
    def print_stack(self):
        print(self.data)