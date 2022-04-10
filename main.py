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

    def pop_first(self):
        if self.head is None:
            return None
        elif self.length==1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp.value
        else:
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            temp.next = None
            return temp.value

    def get(self, index):
        if index <0 or index > self.length:
            return None
        else:
            temp = self.head
            for ind in range(index):
                temp = temp.next
            return temp.value

    def set(self, index, value):
        if index < 0 or index >self.length:
            return False
        else:
            temp = self.head
            for ind in range(index):
                temp = temp.next
            temp.value = value
            return True

    def insert(self, index, value):
        if index <0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            temp = self.head
            for ind in range(index):
                temp = temp.next
            new_node = Node(value)
            temp.prev.next = new_node
            new_node.prev = temp.prev
            new_node.next = temp
            temp.prev = new_node
            self.length +=1
            return True

    def remove(self, index):
        if index <0 or index > self.length:
            return False
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            temp = self.head
            for ind in range(index):
                temp = temp.next
            before = temp.prev
            after =temp.next
            before.next = after
            after.prev = before
            tem.next = None
            temp.prev = None
            self.length -= 1
            return temp.value

my_DLL= DoublyLinkedList(7)
my_DLL.append(3)
my_DLL.append(5)
x = my_DLL.pop()
my_DLL.prepend(1)
my_DLL.print_list()
my_DLL.set(0,10)
my_DLL.insert(1,100)
my_DLL.insert(4,200)
my_DLL.remove(2)
my_DLL.print_list()
