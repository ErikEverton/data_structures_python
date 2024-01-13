class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f'{self.value}, {self.next}'


class Stack:
    def __init__(self) -> None:
        self.top = Node()
    
    def isEmpty(self):
        if self.top.value is None:
            return True
        return False
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    

    def __repr__(self) -> str:
        return f'[{self.top.value}, {self.top.next}]'
