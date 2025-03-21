from time import sleep


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 가장 마지막에 있는 값들을 항상 head의 위치에 두어야 확인하기 수월함

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            print("bro, stack is empty")
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            print("bro, stack is empty")
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):

        return self.head.data


stack = Stack()
stack.push(4)
print(stack.peek())
stack.push(5)
print(stack.peek())
stack.push(3)
print(stack.peek())

