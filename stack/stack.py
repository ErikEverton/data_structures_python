class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f'{self.value}, {self.next}'


class Stack:
    def __init__(self) -> None:
        self.top = None
    
    def isEmpty(self):
        if self.top.value is None:
            return True
        return False
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        last_top = self.top
        self.top = self.top.next
        return last_top.value

    def peek(self):
        return self.top.value

    def __repr__(self) -> str:
        return f'[{self.top.value}, {self.top.next}]'
    


# Some tests
    
stack = Stack()

for n in range(0, 10):
    stack.push(n)

for n in range(0, 5):
    stack.pop()

print(stack)
print(stack.pop())
print(stack.peek())
