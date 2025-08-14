from node import Node


class LinkedList:
    def add_to_tail(self, node):
        # If the list is empty, set head to the new node
        if self.head == None:
            self.head = node
        else:
            # Otherwise, traverse to the last node
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            # Set the last node's next to the new node
            last_node.next = node

    # don't touch below this line

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)

