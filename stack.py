class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f'{self.value}, {self.next}'


class Stack:
    def __init__(self) -> None:
        self.top = None
    
    def isEmpty(self, value):
        if self.top is None:
            return True
        return False
    
    