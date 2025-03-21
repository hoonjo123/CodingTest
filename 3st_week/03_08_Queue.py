class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        # 아무것도 queue에 들어가있지 않은 상태라면 에러가 발생해버림,

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return


        self.tail.next = new_node
        self.tail = new_node
        return

    def dequeue(self):
        if self.is_empty():
            return "큐에 아무것도 없는데요?"

        deleted_head = self.head
        self.head = self.head.next
        return deleted_head.data

    def peek(self):
        if self.is_empty():
            return "큐에 아무것도 없는데요?"

        return self.head.data

    def is_empty(self):

        return self.head is None

queue = Queue()
queue.enqueue(4)
print(queue.peek())
queue.dequeue()
queue.enqueue(2)
print(queue.peek())
queue.dequeue()
queue.enqueue(3)
print(queue.peek())
