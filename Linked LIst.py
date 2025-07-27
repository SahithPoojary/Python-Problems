class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def add_data(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete1(self, pos):
        if self.head is None:
            print("Delete not possible, list is empty.")
            return

        if pos == 1:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 1

        while current and count < pos:
            prev = current
            current = current.next
            count += 1

        if current is None:
            print("Position not found.")
            return

        prev.next = current.next

l = LinkedList()
l.add_data(20)
l.add_data(28)
l.add_data(30)
l.add_data(21)
l.add_data(26)

print("Before deletion:")
l.display()

l.delete1(3)

print("After deletion:")
l.display()
