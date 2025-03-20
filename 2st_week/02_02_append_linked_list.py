class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


node = Node(3)
print(node.data, node.next)

first_node = Node(5)

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index += 1

        return cur

linked_list = LinkedList(5)
linked_list.append(12)

print(LinkedList.get_node(1).data)