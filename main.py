class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None :
            self.tail = new_node
            self.head = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1
            return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            slef.length = 1
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length +=1
        return True




my_DLL= DoublyLinkedList(7)
my_DLL.append(3)
my_DLL.append(5)
x = my_DLL.pop()
my_DLL.prepend(1)
my_DLL.print_list()
