class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        node = Node(data)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def push(self, data):
        node = Node(data)
        if not self.tail and not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def pop(self):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev.next = None
                self.head.prev = None

    def dequeue(self):
        if self.tail:
            if self.tail == self.head:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next.prev = None
                self.tail.next = None

    def display_inorder(self):
        result = []
        i = self.head
        while i:
            result.append(i.data)
            i = i.next
        print(result)

    def display_reverse(self):
        result = []
        i = self.tail
        while i:
            result.append(i.data)
            i = i.prev
        print(result)

    def replace(self, existing, new, all=False):
        i = self.head
        while i:
            if i.data == existing:
                i.data = new
                if not all:
                    break
            i = i.next

    def update(self, index, val):
        count = 1
        i = self.head
        while i:
            if count == index:
                i.data = val
                break
            i = i.next
            count += 1

if __name__ == "__main__":
    dll = DLL()
    dll.enqueue(23)
    dll.enqueue(23)
    dll.enqueue(23)
    dll.enqueue(23)
    dll.enqueue(90)
    dll.enqueue(23)

    # dll.enqueue(48)
    # dll.enqueue(19)
    # dll.enqueue(78)
    # dll.enqueue(22)
    # dll.enqueue(45)
    # dll.push(23)
    # dll.push(923)
    # dll.push(3)
    # dll.push(2)
    # dll.push(87)
    # dll.push(34)
    # dll.push(76)
    # dll.push(12)
    # dll.push(98)
    # dll.push(54)

    dll.display_inorder()
    dll.display_reverse()

    # dll.pop()
    # dll.dequeue()

    # dll.replace(23, 45, True)
    dll.update(3, 99)

    dll.display_inorder()
    dll.display_reverse()
