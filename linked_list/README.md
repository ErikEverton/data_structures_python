#What are linked lists? 

A linked list is a sequence of cells. Each cell has an object and the address to the next cell. If the address of the next cell is None that means that the linked list ends there. The first cell in the linked list is called head and the last one is called tail.
Each cell of the list is a node and a node consists of two fields one is the data and the other is a reference to the next node in the list.
Each node of the list can be anywhere in the memory, because the node before will always point to it. 
To insert an element in the start of the list the time complexity is O(1), because we will just made it point the the first pointer.
But to insert in the middle of the list the time complexity is O(n), because we don't know how many elements we have until we find the place the element needs to be.
To delete the first node is easy, beacause we just need to make the head be the second node. To delete the fist element the time complexity is O(1). To delete middle elements the time complexity is O(n)