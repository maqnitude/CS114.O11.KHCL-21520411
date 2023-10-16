class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head # type: ignore
            self.head.prev = new_node # type: ignore
            self.head = new_node

    def insert_after(self, target, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            current = self.head
            while current:
                if current.data == target:
                    new_node.prev = current # type: ignore
                    new_node.next = current.next
                    if current.next:
                        current.next.prev = new_node
                    else:
                        self.tail = new_node
                    current.next = new_node # type: ignore
                    return
                current = current.next

            # insert to head if not found
            new_node.next = self.head # type: ignore
            self.head.prev = new_node # type: ignore
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        # if tail doesn't exsist then head also doesn't exist
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail # type: ignore
            self.tail.next = new_node # type: ignore
            self.tail = new_node

    def delete_head(self):
        if not self.head:
            return
        else:
            if not self.head.next:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

    def _remove(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None

    def delete(self, target):
        if not self.head:
            return
        else:
            current = self.head
            while current:
                if current.data == target:
                    self._remove(current)
                    return
                current = current.next

    def delete_all(self, target: int):
        if not self.head:
            return
        else:
            current = self.head
            while current:
                next_node = current.next
                if current.data == target:
                    self._remove(current)
                current = next_node

    def print_list(self):
        if not self.head:
            print("blank")
        else:
            current = self.head
            output = []
            while current:
                output.append(str(current.data))
                current = current.next
            print(' '.join(output))

dllist = DoublyLinkedList()
while True:
    line = list(map(int, input().split()))
    
    op = line[0]
    
    if op == 0:
        dllist.insert(*line[1:])
    elif op == 1:
        dllist.append(*line[1:])
    elif op == 2:
        dllist.insert_after(*line[1:])
    elif op == 3:
        dllist.delete(*line[1:])
    elif op == 4:
        dllist.delete_all(*line[1:])
    elif op == 5:
        dllist.delete_head()
    elif op == 6:
        dllist.print_list()
        break
