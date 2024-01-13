class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    def __repr__(self) -> str:
        return f'{self.value}, {self.next}'


class Queue:
    def __init__(self) -> None:
        self.front = None
    
    def __repr__(self) -> str:
        return f'[{self.front}]'

    def isEmpty(self):
        if self.front is None:
            return True
        return False

    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.front = new_node
            return
        current = self.front
        while current:
            if current.next is None:
                current.next  = new_node
                return
    


#Tests 

queue = Queue()
queue.enqueue(1)
print(queue)
