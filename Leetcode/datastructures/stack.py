class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack = self.stack[:-1]
        
    def peek(self):
        print(self.stack[-1])
    
    def print_stack(self):
        print(self.stack)

my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

my_stack.print_stack()
my_stack.pop()
my_stack.print_stack()