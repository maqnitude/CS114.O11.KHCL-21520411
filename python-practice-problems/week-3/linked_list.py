class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = {}

    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head # type: ignore
            self.head.prev = new_node # type: ignore
            self.head = new_node

        if data in self.nodes:
            self.nodes[data].insert(0, new_node)
        else:
            self.nodes[data] = [new_node]

    def insert_after(self, target, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            if target in self.nodes:
                target_node = self.nodes[target][0]

                new_node.prev = target_node
                new_node.next = target_node.next
                if target_node.next:
                    target_node.next.prev = new_node
                else:
                    self.tail = new_node
                target_node.next = new_node

                if data in self.nodes:
                    self.nodes[data].append(new_node)
                else:
                    self.nodes[data] = [new_node]
            else:
                new_node.next = self.head # type: ignore
                self.head.prev = new_node # type: ignore
                self.head = new_node

                if data in self.nodes:
                    self.nodes[data].insert(0, new_node)
                else:
                    self.nodes[data] = [new_node]
            
    def append(self, data):
        new_node = Node(data)

        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail # type: ignore
            self.tail.next = new_node # type: ignore
            self.tail = new_node

        if data in self.nodes:
            self.nodes[data].append(new_node)
        else:
            self.nodes[data] = [new_node]

    def delete_head(self):
        if not self.head:
            return
        else:
            node_to_delete = self.head

            if not self.head.next:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

            if node_to_delete.data in self.nodes and self.nodes[node_to_delete.data]:
                self.nodes[node_to_delete.data].pop(0)
            if not self.nodes[node_to_delete.data]:
                del self.nodes[node_to_delete.data]
        
    def delete(self, target):
        if not self.head:
            return
        else:
            if target in self.nodes:
                node_to_delete = self.nodes[target][0]
                data_to_delete = node_to_delete.data

                if node_to_delete == self.head:
                    if not self.head.next:
                        self.head = self.tail = None
                    else:
                        self.head = self.head.next
                        self.head.prev = None

                    if self.nodes[data_to_delete]:
                        self.nodes[data_to_delete].pop(0)
                    if not self.nodes[data_to_delete]:
                        del self.nodes[data_to_delete]
                elif node_to_delete == self.tail:
                    if not self.tail.prev: # type: ignore
                        self.head = self.tail = None
                    else:
                        self.tail = self.tail.prev # type: ignore
                        self.tail.next = None

                    if self.nodes[data_to_delete]:
                        self.nodes[data_to_delete].pop(0)
                    if not self.nodes[data_to_delete]:
                        del self.nodes[data_to_delete]
                elif node_to_delete.prev and node_to_delete.next:
                    prev_node = node_to_delete.prev
                    next_node = node_to_delete.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    node_to_delete.prev = node_to_delete.next = None

                    if self.nodes[data_to_delete]:
                        self.nodes[data_to_delete].pop(0)
                    if not self.nodes[data_to_delete]:
                        del self.nodes[data_to_delete]

    def delete_all(self, target):
        if not self.head:
            return
        else:
            while target in self.nodes:
                node_to_delete = self.nodes[target][0]
                data_to_delete = node_to_delete.data

                if node_to_delete == self.head:
                    if not self.head.next: # type: ignore
                        self.head = self.tail = None
                    else:
                        self.head = self.head.next # type: ignore
                        self.head.prev = None

                    if self.nodes[data_to_delete]:
                        self.nodes[data_to_delete].pop(0)
                    if not self.nodes[data_to_delete]:
                        del self.nodes[data_to_delete]
                elif node_to_delete == self.tail:
                    if not self.tail.prev: # type: ignore
                        self.head = self.tail = None
                    else:
                        self.tail = self.tail.prev # type: ignore
                        self.tail.next = None

                    if self.nodes[data_to_delete]:
                        self.nodes[data_to_delete].pop(0)
                    if not self.nodes[data_to_delete]:
                        del self.nodes[data_to_delete]
                elif node_to_delete.prev and node_to_delete.next:
                    prev_node = node_to_delete.prev
                    next_node = node_to_delete.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    node_to_delete.prev = node_to_delete.next = None

                    if self.nodes[data_to_delete]:
                        self.nodes[data_to_delete].pop(0)
                    if not self.nodes[data_to_delete]:
                        del self.nodes[data_to_delete]

    def print_list(self):
        if not self.head:
            print("blank")
        else:
            output = ""
            current = self.head
            while current:
                output += str(current.data)
                if current.next:
                    output += " "
                current = current.next
            print(output)

dllist = DoublyLinkedList()
while True:
    line = input().split()
    
    if len(line) == 1:
        op = int(line[0])
        if op == 5:
            dllist.delete_head()
        elif op == 6:
            dllist.print_list()
            break
    elif len(line) == 2:
        op, data = list(map(int, line))
        if op == 0:
            dllist.insert(data)
        elif op == 1:
            dllist.append(data)
        elif op == 3:
            dllist.delete(data)
        elif op == 4:
            dllist.delete_all(data)
    elif len(line) == 3:
        op, target, data = list(map(int, line))
        if op == 2:
            dllist.insert_after(target, data)
