class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insertbeg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def deletenode(self, key):
        current = self.head


        if current and current.data == key:
            self.head = current.next
            current = None
            return

  
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next


        if current is None:
            return

        prev.next = current.next
        current = None

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertend(1)
    ll.insertend(2)
    ll.insertend(3)
    ll.display() 

    ll.insertbeg(0)
    ll.display() 

    ll.deletenode(2)
    ll.display()