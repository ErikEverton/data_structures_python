class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f'{self.value}, {self.next}'
    

class LinkedList:
    def __init__(self, head) -> None:
        first_node = Node(head)
        self.head = first_node
        self.tail = first_node

    def __repr__(self):
        return f'[{self.head}]'
    
    def initial_insertion(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def intermediate_insertion(self, before, value):
        new_node = Node(value)
        next_node = before.next
        before.next = new_node
        new_node.next = next_node
        if new_node.next is None:
            self.tail = new_node
    
    def insertion_at_the_end(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
    
    def delete(self, value):
        current = self.head

        if value == self.head.value:
            self.head = self.head.next
            return

        while current:
            next_node = current.next
            if next_node:
                if next_node.value == value:
                    current.next = next_node.next
                else:
                    current = next_node
            current = next_node

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None
    

#Some tests 

list = LinkedList(0)

for n in range(1, 5):
    list.initial_insertion(n)

list.delete(2)

current = list.head

search = list.search(3)

list.intermediate_insertion(before=search, value=5)
list.insertion_at_the_end(6)
list.insertion_at_the_end(7)

while current:
    print(current.value)
    current = current.next

print(list)
