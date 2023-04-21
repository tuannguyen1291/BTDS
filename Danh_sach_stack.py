class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.top.data

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop()) # In ra 3
print(stack.peek()) # In ra 2
print(stack.pop()) # In ra 2
print(stack.pop()) # In ra 1
print(stack.is_empty()) # In ra True
