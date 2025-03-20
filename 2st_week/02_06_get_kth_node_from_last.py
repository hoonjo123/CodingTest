# Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # def get_kth_node_from_last(self, k):
    #
    #     # 끝에 값을 먼저 알아야겠다.
    #     length = 1 # head노드부터 시작하면 길이는 1이다.
    #     cur = self.head
    #
    #     while cur.next is not None:
    #         cur = cur.next
    #         length += 1
    #
    #     # print("length의 전체 길이: ", length) #전체의 길이는 3으로 나온다.
    #     # 전체길이의 끝에서 k번째이기 때문에 cur노드를 end_length라는 곳 까지만 이동하도록 한다.
    #     end_length = length - k # 3에서 -k를 뺀 길이
    #     cur = self.head # 다시 head노드로 이동
    #
    #     for i in range(end_length):
    #         #end_length의 길이만큼 이동
    #         cur = cur.next
    #
    #     return cur

    ########################### 위 코드를 좀 더 개선해보자.#################################
    # 투포인터를 이용하면 될것같다.
    # slow와 fast 두 점을 두고 항상 k만큼 떨어진 상태로 노드를 순회하도록 한다.
    # 예를 들어,
    #
    # head
    # slow          fast
    #       slow          fast
    #              slow          fast
    #                      slow           fast
    # [6] -> [7] -> [8] -> [9] -> [10] -> [11]
    # 항상 k만큼 떨어져 있는데, fast가 노드의 끝에 도달한 순간,
    # slow의 위치를 통해 끝에서 k번째의 값을 도출할 수 있다
    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next # fast를 먼저 k만큼 이동시킨다.

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow

    # 사실상 시간복잡도에서는 큰 차이가 없음
    #
linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!