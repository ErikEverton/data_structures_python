class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    

class LinkedList:
    def __init__(self, head) -> None:
        first_node = Node(head)
        self.head = first_node
    
    def insert_at_the_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, value):
        current = self.head

        if value == self.head.value:
            self.head = self.head.next

        while current:
            next = current.next
            if next:
                if next.value == value:
                    current.next = next.next
                else:
                    current = next
            current = next


list = LinkedList(0)

for n in range(1, 5):
    list.insert_at_the_beginning(n)

list.delete(2)

current = list.head

while current:
    print(current.value)
    current = current.next
