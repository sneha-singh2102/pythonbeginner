class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.prev = None
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        linkedliststring = ''
        while itr:
            linkedliststring += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print("Traversal in forward direction: ", linkedliststring)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.get_last_node()
        linkedliststring = ''
        while itr:
            linkedliststring += str(itr.data) + ' <-- ' if itr.prev else str(itr.data)
            itr = itr.prev
        print("Traversal in backward direction: ", linkedliststring)

    def get_last_node(self):
        iterator = self.head
        while iterator.next is not None:
            iterator = iterator.next
        return iterator

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node  # set the current head prev pointer to new node
            self.head = node  # set the head to new node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at_index(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def delete_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    llist = DoubleLinkedList()
    llist.insert_values(["banana", "mango", "grapes", "orange"])
    llist.print_forward()
    llist.print_backward()
    llist.insert_at_end("figs")
    llist.print_forward()
    llist.insert_at_index("jackfruit", 0)
    llist.print_forward()
    llist.insert_at_index("dates", 6)
    llist.print_forward()
    llist.insert_at_index( "kiwi", 2)
    llist.print_forward()
    llist.delete_at_index( 2)
    llist.print_forward()
