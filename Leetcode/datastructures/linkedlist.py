class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        curr = self.head
        nodes = []
        while curr is not None:
            nodes.append(curr.data)
            curr = curr.next
            
        nodes.append("None")
        return " -> ".join(nodes)

    def insertEnd(self, new_node):
        curr = self.head
        # Does the linked list have any elements
        if not self.head:
            self.head = new_node
            return
        
        # Traverse through the list until curr.next is None
        while curr.next:
            curr = curr.next
        curr.next = new_node
            

    def insertBeginning(self, new_node):
        if not self.head:
            self.head = new_node

        second_node = self.head
        self.head = new_node
        new_node.next = second_node

    def insertAtPosition(self, new_node, position):
        if not self.head:
            print('LL Empty')
            return
        
        pos_counter = 1
        curr = self.head
        if position == 1:
            new_node.next = self.head
            self.head = new_node
        while curr:
            if position+1 == pos_counter:
                new_node.next = curr.next
                curr.next = new_node
                return
            else:
                pos_counter += 1
                curr = curr.next

    def remove_element(self, value):
        # Checking if the LL is empty
        if not self.head:
            print('Linked list empty')
            return
        
        curr = self.head
        # Element to remove is at the first position
        if curr.data == value:
            self.head = curr.next
            return

        while curr.next:
            print(curr.next.data)
            if curr.next.data == value:
                curr.next = curr.next.next
                return
            curr = curr.next
            
        print('Element not found')
        





llist = LinkedList()
print(llist)

first_node = Node("a")
llist.head = first_node
second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
fourth_node = Node('d')
llist.insertEnd(fourth_node)
fifth_node = Node('e')
llist.insertBeginning(fifth_node)
sixth_node = Node('f')
llist.insertAtPosition(sixth_node, 2)
print(llist)
llist.remove_element('z')
print(llist)
