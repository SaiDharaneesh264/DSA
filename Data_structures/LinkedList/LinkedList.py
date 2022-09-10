class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            print('first data:', last_node.data)
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
    def insert_after_node(self, after_data, data):
        new_node = Node(data)
        cur_node = self.head
        if (cur_node and cur_node.data == after_data):
            new_node.next = cur_node.next
            cur_node.next = new_node
            return
        prev_node = None
        while cur_node and cur_node.data != after_data:
            prev_node = cur_node
            cur_node = cur_node.next
        new_node.next = cur_node.next
        cur_node.next = new_node

    def insert_before_node(self, prev_data,  data):
        if self.head and self.head.data == prev_data:
            self.prepend(data)
            return
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next and cur_node.next.data != prev_data:
            cur_node = cur_node.next
        new_node.next = cur_node.next
        cur_node.next = new_node
        # 1 2 3 4 5

        
    def print_list(self):
        cur_node = self.head
        while cur_node.next:
            print(cur_node.data, end=", ")
            cur_node = cur_node.next
        print(cur_node.data)

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
ll.print_list()
ll.insert_after_node(3, 4)
ll.print_list()
ll.insert_before_node(4, 6)
ll.print_list()
